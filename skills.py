#!/usr/bin/env python3
# -*- encoding=utf-8 -*-


import sys
import os
import json
import random
from dueros.Bot import Bot

from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1

from dueros.card.ImageCard import ImageCard
from dueros.card.ListCard import ListCard
from dueros.card.ListCardItem import ListCardItem
from dueros.card.StandardCard import StandardCard
from dueros.card.TextCard import TextCard

class PuGongYing(Bot):

    def __init__(self, data):

        super().__init__(data)
        self.data = data
        # main intent
        self.add_launch_handler(self.launchRequest)
        self.add_intent_handler('welcome', self.welcome)
        self.add_intent_handler('next_one', self.next_one)
        self.add_intent_handler('answer', self.answer)
        self.add_intent_handler('answer_helper', self.answer_helper)
        self.add_intent_handler('c_game', self.c_game)
        self.add_intent_handler('more_one', self.more_one)
        self.add_intent_handler('ai.dueros.common.default_intent', self.quesheng)
        # idiom intent
        self.add_intent_handler('start_IdiomC', self.start_IdiomC)
        self.add_intent_handler('tell_idiom_story', self.tell_idiom_story)
        self.add_intent_handler('start_IdiomGuess', self.start_IdiomGuess)
        # english intent
        self.add_intent_handler('study_english_word', self.study_english_word)
        self.add_intent_handler('tell_english_joke', self.tell_english_joke)
        self.add_intent_handler('tell_english_story', self.tell_english_story)
        self.add_intent_handler('english_songs', self.english_song)
        # english data
        self.english_song = [
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', '']
        ]
        self.english_joke = [
            ['Teacher: whoever answers my next question, can go home.老师：谁能回到我下一个问题，谁就可以回家了。One boy throws his bag out the window.一个小男孩把书包扔到窗外。Teacher: who just threw that?!老师：谁刚刚把书包扔出去了?Boy: Me! I’m going home now.男孩：我!我现在要回家了。', ''],
            ['What dog can jump higher than a building?什么狗比大楼跳的还高?Anydog, buildings cannot jump!任何一只狗，大楼又跳不起来。', ''],
            ["Sister's boyfriend: No, dont do that. Here is a nickel.Little brother: That makes a buck and a quarter I love made this mont弟弟：我看见你亲我姐姐了，如果你不给我五分钱，我就告诉我爸。姐姐的男朋友：不要那样做。给你五分钱。弟弟：我这个月已经赚了一块两毛五了。", ''],
            ["Dentist: I'm sorry, madam, but I'll have to charge you twenty-five dollars for pulling your son's tooth.Mother: Twenty-five dollars! But I thought you only charged five dollars for an extraction.Dentist: I usually do. But your son yelled so loud, he scared four other patients out of the office.牙科医生：对不起，夫人，为给您的儿子拔牙，我得收二十五美元。母亲：二十五美元!可是我知道您拔一颗牙只要五美元呀?牙科医生：是的。但是您儿子这么大声地叫唤，他都吓跑四位病人了。", ""],
            ["Younger Scout: How can I tell the difference between a mushroom and a toadstool?Older Scout: Just eat one before you go to bed. If you wake up the next morning, it was a mushroom.年少的童子军：我怎样才能把蘑菇和毒蕈区别开呢?年长的童子军：上床前吃一个。如果你第二天早上醒来，那就是蘑菇。", ""],
            ["‘Do you believe in life after death?’the boss asked one of his employees. ‘Yes, Sir.’ the new recruit replied.‘Well, then, that makes everything just fine,’ the boss went on. 'After you left early yesterday to go to your grandmother's funeral, she stopped in to see you.“你相信人能死后重生吗?”老板问他的一个员工。 “我相信，先生”。这位刚上班不久的员工回答。 “哦，那还好”。老板接着说。 “你昨天提早下班去参加你祖母的葬礼后，她老人家到这儿看你来了。”", ""],
            ["The fine-furniture store where I work has been in business since the 1920s. Recently I received a call from a woman who wanted to replace some chairs from a dining set purchased from us in the 1930s. I assured her we could help and sought the assistance of the office manager. “You'll never believe this one, ”I told him.“ I just got a call from a customer who bought some chairs from us in the 1930s. ”Before I could finish repeating her request, he interrupted and said, “Don't tell me she hasn't received them yet!”我所工作的精品家具商店是从20世纪二十年代以来就营业的。最近我接到一个妇女的电话。她想换一套餐具中的一些椅子。这套餐具她是在三十年代从我们这儿买的。我向她保证说我们可以帮她的忙，于是我向部门经理寻求帮助。“你永远也不会相信，”我对他说，“我刚接到一个顾客的电话，她在三十年代从我们这里买了一些椅子。” 我还没来得及说她的要求，经理就打断了我的话：“你别告诉我她到现在还没收到货!”", ""],
            ["A husband and wife,both 91,stood before a judge,asking for a divorce.“I don't understand,”He said,“Why do you want a divorce at this time of life?”the husband explained “Well , you see,We wanted to wait until the children died.”有一个丈夫和妻子都是91岁，他们站在法官面前，要求离婚。“我不明白，”法官说，“你们为什么到了这把年纪还要离婚?”丈夫解释道：“嗯，你是知道的，我们以前是哟等到孩子们都死了。”", ""],
            ["Teacher: What is the plural of man,Tom?Tom: Men.Teacher: Good. And the plural of child?Tom : Twins.老师: 汤姆，“男人”这个词的复数形式是什么?汤姆:男人们。老师: 答得好。那“孩子”的复数形式呢?汤姆: 双胞胎", ""],
            ["Mike was late for school. He said to his teacher, Mr. Black, “Excuse me for my coming late, sir. I watched a football match in my dream.”“Why did it make you late?”inquired the teacher.　“Because neither team could win the game, so it lasted a long time.” replied Mike.麦克上学迟到了。他对布莱克老师说：“对不起，老师，今天早上我迟到了。因为我在梦里观看了一场球赛。”“为什么它会让你迟到呢?”老师问道。因为这两个队都没有能力获胜，所以就持续的时间长了。”麦克回答说。", ""],
            ["After burying his mother nine months earlier, a client of the local mortuary finally had enough money to purchase the expensive coffin he'd originally wanted. So we exhumed the body and transferred his deceased mother into the new steel casket. “What's so special about this coffin?” I asked the funeral director. He replied, “It has a lifetime warranty.”在将母亲下葬9个月后，当地殡仪馆的一个客户终于攒够了钱去买那副他早就相中的价值不菲的棺材了。他把母亲的棺材挖了出来，将尸体转移到了那副新的钢制棺材中。“这副棺材有什么特别?”，我问葬礼的承办人。他回答说，“这种棺材终生保修", ""],
            ["“Oh, my poor man,”exclaimed the kind old lady， “It must be dreadful to be lame. But it would be much worse if you were blind.”“You're absolutely right,”said the beggar, obviously an old hand at the game.“When I was blind, people kept giving me foreign coins.”“啊，可怜的人。”善良的老妇人惊叹道。“脚瘸就够惨的了，要是眼瞎就更糟了。”“你说的一点儿没错。”那乞丐说。他显然是乞讨老手。“我眼瞎的时候，人们老是给我外币。”", ""],
            ["A newspaper organized a contest for the best answer to the question: “If a fire broke out in the Louvre, and if you could only save one painting, which one would you carry out?”The winning reply was: “The one nearest the exit.”一份报纸组织了一场竞赛，为下面的问题征集最佳答案：“如果卢浮宫起了火，而你只能救出一幅画，你将救出哪一幅?”获奖的答案是：“最接近门口的那一幅。”", ""],
            ["A friend and I were standing in line at a fast-food restaurant, waiting to place our order. There was a big sign posted. “No bills larger than $20 will be accepted.”我和一个朋友在快餐店排队订餐，那里很醒目地写着，不接受超过20美元的大钞(请自备零钱)。The woman in front of us, pointing to the sign, remarked, “Believe me, if I HAD a bill larger than $20, I wouldn't be eating here.”我们前边的一个女士指着这个牌子对我们说：“上帝保佑，如果我身上有超过20美元的话，我一定不会在这儿吃饭!”", ""],
            ["A man walks into a bar and orders a beer. He takes his first sip and sets it down. While he is looking around the bar, a monkey swings down and steals the pint of beer from him before he is able to stop the monkey.一男子去酒吧，点了一杯啤酒。他喝了一口放下。当他环视酒吧时，发现一只猴子荡下来，在他阻止之前，偷走了啤酒。The man asks the barman who owns the monkey. The barman replies the piano player. The man walks over to the piano player and says “Do you know your monkey stole my beer.” The pianist replies “No, but if you hum it, I'll play it.”该男子问酒吧招待，这只猴子是谁的。服务员回答说是钢琴手的。男子走到钢琴手面前问：“你知道你的猴子偷了我的啤酒吗?”钢琴手回答说：“没有，但是如果你能哼唱，我会为你演奏的。”", ""],
            ["One day, Bill and Tom went to a restaurant for dinner. As soon as the waiter took out two steaks, Bill quickly picked out the bigger steak for himself.一天，比尔和汤姆去餐馆吃饭。当服务员端上两份牛排时，比尔迅速地为自己拿了比较大的那块。Tom wasn't happy about that: “When are you going to learn to be polite?”汤姆对此很不开心：“你什么时候能学会礼貌?”Bill: “If you had the chance to pick first, which one would you pick?”比尔说：“如果让你先拿，你会拿哪个?”Tom: “The smaller piece, of course.”汤姆说：“当然是小的那个。”Bill: “What are you whining about then? The smaller piece is what you want, right?”比尔：“那你还抱怨什么?小的那个不就是你想要的，不是吗?”", ""],
            ["As the taxi came to a screeching halt at a traffic light, I asked the driver, “Do you agree that 'Time is money'?”出租车在遇到红灯急刹车时，我问司机：“你同意‘时间就是金钱’这种说法吗?”“Well, it's a very common saying. Who will care so much about that?” the driver answered.“哦，这是一个普遍说法。在这个问题上，谁会在意那么多呢?”司机回答说。“Look, the digits in the meter are still running when the car has stopped, ”I pointed at the meter.“看，在车已经停止的情况下，里程表上的数字还在跑。”我指着里程表说。“Oh, yes. You've got a point here. In this case, time is money for both of us. added the driver.“哦，是的。你说的挺有道理的。在这种情况下，时间对我们俩来说都是金钱。”司机补充说。“", ""],
            ["Q: Why won’t the elephant use the computer?A: He’s afraid of the mouse!鼠标和老鼠的英文皆为mouse", ""],
            ["Q: Which are the stronger days of the week?A: Saturday and Sunday. The rest are weekdays.week和weak同音：", ""],
            ["Q: Which runs faster, hot or cold?A: Hot. Everyone can catch a cold.catch有抓住的意思，catch a cold是感冒的意思", ""],
            ["Q: How did the soldier fit his tank in his house?A: It was a fish tank.tank n. 坦克；水槽；池塘fish tank  鱼缸，金鱼缸", ""],
            ["Q: How can you tell the ocean is friendly?A: It waves.wave有波涛翻滚的意思，也有挥手致意的意思", ""],
            ["A little rabbit is happily running through the forest when he stumbles upon a giraffe rolling a joint. The rabbit looks at her and says, “Giraffe my friend, why do you do this? Come with me running through the forest, you'll feel so much better!” The giraffe looks at him, looks at the joint, tosses it and goes off running with the rabbit.有一只小白兔快乐地奔跑在森林中, 在路上它碰到一只正在卷大麻的长颈鹿。小白兔看着长颈鹿说道：“长颈鹿我的朋友，你为什么要做这种事呢？和我一起在森林中奔跑吧，你会感觉心情舒畅很多！”长颈鹿看看小白兔，又看看手里的大麻烟，把大麻烟向身后一扔，跟着小白兔在森林中奔跑。Then they come across an elephant doing coke, so the rabbit again says, “Elephant my friend, why do you do this? Think about your health. Come running with us through the pretty forest, you'll feel so good! The elephant looks at them, looks at his coke, then tosses it and starts running with the rabbit and giraffe 后来它们遇到一只正准备吸食可卡因的大象，小白兔又对大象说：“大象我的朋友，你为什么要做这种事呢？想想自己的健康啊。跟我们一起在这片美丽的森林中奔跑吧，你会感觉好很多！”大象看看它们，又看看手中的可卡因，于是把可卡因向身后一扔，跟着小白兔和长颈鹿一起奔跑。he three animals then come across a lion about to shoot up and the rabbit again says, “Lion my friend, why do you do this? Think about your health! Come running with us through the sunny forest, you will feel so good!”后来它们遇到一只正准备注射毒品的狮子，小白兔又对狮子说：“狮子我的朋友，你为什么要做这种事呢？想想自己的健康啊！跟我们一起在这片阳光明媚的森林中奔跑吧，你会感觉如此美好！The lion looks at him, puts down his needle, and starts to beat the hell out of the rabbit. As the giraffe and elephant watch in horror, they look at him and ask, ”Lion, why did you do this? He was merely trying to help us all!狮子看看小白兔，放下手中的针筒，把小白兔猛揍了一顿。长颈鹿和大象被吓坏了，它们看着狮子问它：“狮子，你为什么要打小白兔呢？它只是想要帮助我们大家啊！The lion answers, “He makes me run around the forest like an idiot each time he's on ecstasy!狮子回答：“这家伙每次嗑了摇头丸就拉着我像白痴一样在森林里乱跑！”", ""],
            ["A man walks into a bar and orders a beer. He takes his first sip and sets it down. While he is looking around the bar, a monkey swings down and steals the pint of beer from him before he is able to stop the monkey.一男子去酒吧，点了一杯啤酒。他喝了一口放下。当他环视酒吧时，发现一只猴子荡下来，在他阻止之前，偷走了啤酒。The man asks the barman who owns the monkey. The barman replies the piano player. The man walks over to the piano player and says “Do you know your monkey stole my beer.” The pianist replies ”No, but if you hum it, I'll play it.该男子问酒吧招待，这只猴子是谁的。服务员回答说是钢琴手的。男子走到钢琴手面前问：“你知道你的猴子偷了我的啤酒吗?”钢琴手回答说：“没有，但是如果你能哼唱，我会为你演奏的。”", ""],
            ["A friend and I were standing in line at a fast-food restaurant, waiting to place our order. There was a big sign posted. ", ""],
            ["a wealthy old lady who lived near dr. swift used to send him presents occasionally by her servant. dr. swift took her presents but never gave the boy anything for his trouble. one day as swift was busy with his writing, the boy rushed into his room, knocked some books out of their place, threw his parcel on the desk and said, my mistress has sent you two of her rabbits.在斯威夫特博士家附近，有一位富有的老妇人，她时常打发仆人给他送礼物。斯威夫特博士接受她的礼物，但从不给小厮任何酬谢。一天，斯威夫特博士正忙着写东西，小厮冲进了他的房间，把书一扒拉，将一个包裹扔在书桌上，说道：我的女主人送给你两只兔子。swift turned round and said, my boy, that is not the way to deliver your parcel（包裹） . now, you sit in my chair, watch my way of doing it and learn your lesson. 斯威夫特转过身来说：孩子，包裹可不是这样送法呀。现在，你坐在我的椅子上，看看我是怎么送的，并要记取这个教训。the boy sat down. swift went out, knocked on his door and waited. the boy said, come in. the doctor entered, walked to his desk and said, if you please sir, my mistress sends her kind regards and hopes you will accept these rabbits which her son shot this morning in her fields.小厮坐了下来，斯威夫特走出去，敲了敲门，等待回音。小厮说进来。博士进了门，走到桌旁说道：先生，我的女主人向您致以亲切的问候，并希望您收下这些兔子，这是她儿子今天早晨在地里打的。the boy answered, thank you, my boy, give your mistress and her son my thanks for their kindness and here is two shillings for yourself.小厮回答说：谢谢你，我的孩子。向你的女主人和她的儿子致谢，谢谢他们的关心。这两个先令是送给你本人的。the doctor laughed, and after that, swift never forgot to give the boy his tip.博士笑了，打那以后，斯威夫特从没忘记送小费给小厮。", ""],
            ["joe and fred were helping to build a house in a village. the weather was very warm, there was a lot of dust everywhere, and by half past twelve, they were very thirsty, so they stopped work to have their lunch. they found the nearest small bar, went in and sat down with their sandwiches.乔和佛瑞德在一个村子里帮忙盖一间房子。天气很暖和，到处都有许多灰尘。12点半的时候，他们觉得非常口渴，便停下来去吃午饭了。他们找到最近的一家酒吧，走进去坐下吃他们的三明治。good afternoon, gentlemen. what can i get you? the man behind the bar asked.下午好，先生。你们想要点什么？柜台后面的伺应问道下午好，先生。你们想要点什么？柜台后面的伺应问道joe looked at fred and said, beer, i think. yes, a pint of beer each. is that all right for you, fred?乔看了看佛瑞德说：我想，啤酒吧。好，那就每人一品脱啤酒。这样可以吗，佛瑞德？yes, that's all right. fred said. then he turned to the man behind the bar and said, and i want it in a clean glass! don't forget that好的，可以。佛瑞德说。然后他转过去跟柜台后面的侍应说：我要啤酒装在一个干净的杯子里！别忘了。the man behind the bar filled the glasses and brought them to joe and fred. then he said. which of you asked for the clean glass?.柜台后面的侍应倒满杯子后，拿给乔和佛瑞德，接着说：刚才哪一位要干净的杯子的？", ""],
            ["miles sometime went to the barber's during working hours to have his hair cut. but this was against the office rules: clerks had to have their hair cut in their own time. while miles was at the barber's one day, the manager of the office came in by chance to have his own hair cut and sat just beside him.麦尔斯有时在上班时间去理发馆理发，但这是违反办公室规定的：职员只能利用自己的时间理发。一天，正当麦尔斯理发时，经理碰巧也进来理发，而且就坐在他旁边。hello, miles, the manager said. i see that you are having your hair cut in office time.“你好，麦尔斯，”经理说。我看到你在上班时间理发了”yes, sir, i am,'admitted miles calmly. “you see, sir, it grows in office time.“是的，先生。正是这样。”“麦尔斯平静地承认了。”可先生，你看，头发是在上班时间长的。“not all of it,：“said the manager at once. ”some of it grows in your own time.“不全都是吧，”经理立刻说，“有一些是在你自己的时间里长的。“yes, sir, that's quite true.”answered miles politely, “but i am not having it all cut off.“对呀，先生，你说得很对。“麦尔斯礼貌地回答说，“但我并没有把头发全都剪掉啊。" , ""],
            ["进步:One student to another: “How are your English lessons coming along?“Fine. I used to be one who couldn”t understand the English men, and now it“s the English men who can't understand me.”一位学生对另一位说：“你的英语 最近学的怎么样?”很好，我过去不懂英国人说话，可现在是英国人不懂我的话了。”", ""],
            ["半个还是十分之五:Teacher: Would you rather have one half of an orange or five tenths?Gerald: I'd much rather have the half.Teacher: Think carefully, and tell me why.Gerald: Because you lose too much juice when you cut the orange into five tenths.老师：你愿意要半个柑橘，还是十分之五个柑橘?杰拉得：我宁可要半个。老师：仔细想想，说出理由来。杰拉得：因为你如果把柑橘切成十分之五，那柑橘汁就损失太多了。", ""],
            ["去天堂Sunday School teacher: Hands up all those who want to go to Heaven? Hands up ..... what about you, Terry? You haven't got your hand up -- don't you want to go to Heaven?Terry: I can't. My Mum told me to go straight home.主日学校的教员：想去天堂的人举起手来，把手举起来。。。你呢，哈里?你还没举手呢-- 你不想去天堂吗?哈里： 我去不了，因为妈妈让我一放学就回家。", ""],
            ["Teacher: Now, Jonathan, if I gave you three rabbits and then the next day I gave you five rabbits, how many rabbits would you have?Jonathan: Nine, sir.Teacher: Nine?Jonathan: I've got one already, sir.老师：好，乔纳森，假如我给你三只兔子，第二天我又给你五只，你一共有多少只兔子?乔纳森：一共有九只，先生。老师：九只?乔纳森：先生，我本来就有一只。", ""],
            ["Good BoyLittle Robert asked his mother for two cents. “What did you do with the money I gave you yesterday”“I gave it to a poor old woman，he answered""You're a good boy,said the mother proudly.Here are two cents more. But why are you so interested in the old woman?”“She is the one who sells the candy”""],
            ["Nest and Hair”“My sister a primary school teacher, was informed by one of her pupils that a bird had built its nest in the tree outside the classroom.”“What kind of bird?“my sister asked.”“I didn't see the bird, ma' am, only the nest,“replied the child”“Then, can you give us a description of the nest?” my sister encouraged her”“Well, ma m, it just resembles your hair. ”“],
            ["Just Bitten My Tongue”“Are we poisonous?”“ the young snake asked his mother. ”“Yes, dear,”she replied - Why do you ask?""Cause I've just bitten my tongue!"" ''],
            ["A Woman Who Fell", "It was rush hour and I was dashing to a train in New York City's Grand Central Terminal - As I neared the gate, a plump, middle-aged woman sprinted up from behind, lost her footing on the smooth marble floor and slid onto her back.“r momentum carried her close to my shoes”Before I could help her, however, she had scrambled up.”Gaining her composure, she winked at me and said, “Do you always have beautiful women failing at your feet?"
            ["Q: Which is the strongest creature in the world? ", "A: The snail. It carries its house on its back. "],
            ["Q: What do people do in a clock factory?", "A: They make faces all day. "],
            [" Q: How do you stop a sleepwalker from walking in his sleep? ", "A: Keep him awake."],
            ["Bring me the winner  Waiter, this lobster has only one claw. “i”m sorry, sir. It must have been in a fight. Well, bring me th
            ["The mean man's party. ", "The notorious cheap skate finally decided to have a party. "],
            [" A teacher said to her class:", " was the first man?”“George Washington,”“a little boy shouted promptly”“How do you make out that George Washington was the first man?”asked the teacher, smiling indulgently.”“Because,”said the little boy,“he was first in war, first in peace, and first in the hearts of his countrymen.“But at this point a larger boy held up his hand.“Well,”said the teacher to him, “who do you think was the first man?"],
            ["“How do you make out that George Washington was the first man?“asked the teacher, smiling indulgently.", "“Because, “said the little boy, “he was first in war, first in peace, and first in the hearts of his countrymen.“But at this point a larger boy held up his hand.”the history b“I don't know what his name was,“said the larger boy, “but I know it wasn't George Washington, ma'am, because ook says George Washington married a widow, so, of course, there must have been a man ahead of him."],
            ["There is a little boy and a little girl in the woods.  The little irl asked the boy, What
            [" There is a little boy and a little girl in the woods.  ", "The littlgirl asked the boy, “What is a penis?"
            ["“A married couple on the farm are visited by an alien couple. The alien couple asked the human couple if they would like to swap partners for sex. ", "They agree, the human woman and alien man are together. She says, ”“You have a small penis!”“ The alien man replies, ”“pull my ears!”“ ......A man enters a barber shop for a shaveWhile the barber is foaming him up, he mentions the problem he has getting a close shave around his cheeks. I have just the thing,”“ says the barber, taking a small wooden ball from a nearby drawer. ”“Just place this between your cheek and gum.”“ ......”
            ["”One girl went to the preacher and confessed her sin.", "Girl: Father, I have sinned.”reacher: What did you do, little girl?“irl: Yesterday, I called a man a ”“son of a Bitch.”“"
            ["There was a farmer who raised watermelons. ", "He was doing pretty well but he was disturbed by some local kids who would sneak into his watermelon patch（西瓜地）at night and eat his watermelons. After some careful thought he comes up with a clever idea that he thinks will scare the kids away for sure. So he makes up a sign and posts it in the field. "],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""],
            ["", ""]
        ]
        self.english_story = [
            "这个大家讲的故事主角是狮子，一个狮子在森林里安静的睡觉，一只老鼠沿着他的身体爬了上去，在狮子头顶上玩的特别开心，当狮子醒来后发生了什么事情？它会和老鼠打架吗？从下面的故事中找找答案吧。The ray of the warm sunlight told us that it was spring. A lion was sleeping peacefully in the forest.While the lion was fast asleep, a mouse went on top of the lion. The bold mouse played happily on top of the lion. “Yuppie! This is really fun.” The mouse ran around thumping and stomping here and there.The lion was not able to sleep with all the racket. The lion knew that there was someone on top of him. So, the lion made a surprise attack and rolled on the ground.And the mouse fell over. When the lion saw the mouse he was relieved and said, “Whew! It was only a mouse.”However, far away a fox had seen the scene. The fox laughed mockingly to the lion and said, “You're as big as a mountain and you're afraid of the mouse. You're a coward!” The fox kept making fun of the Lion.Finally the lion spoke, “I wasn't afraid of the mouse. I was only shocked to find a bold enough animal not afraid to run around on top of a lion.“ When the fox heard this he quietly left.”",
            "这个大家讲的故事主角是猴子，据说在从前，树林里有一只猴子，每天猴子都会爬上树看下面的小河看见渔夫扔网与捕鱼。有一天渔民把网放下后吃午饭去了。然后，猴子迅速从树上爬下来跑到河边，模仿渔民的样子撒网，大家想想接下来猴子会撒到鱼吗？会被渔夫逮到吗？从下面的故事中找找答案吧。Once upon a time, there lived a monkey in the woods. The monkey climbed up the tree and looked down at the river everyday.One day, the monkey saw fishermen throw a net over the river. He watched how the fishermen caught fish.Sometime after, the fishermen left the net and went to have lunch. Then, the monkey climbed down from the tree and went to the riverside. The monkey was planning to throw the net like the fishermen did.The monkey was confident since he was good at imitating. Yet, the net wound around the monkey when he touched it. Tied up in the net, the monkey fell into the water.The monkey regretted his behavior, but it was too late. “I should have learned how to use the net before touching it.After believing my prowess and showing off, I am in a bad fix.” The monkey who did not behave carefully drowned in the water.词汇学习：climbed up 爬上fishermen['fiʃəmen]渔夫,钓鱼者climbed down爬下；让步riverside[ˈrɪvəˌsaɪd]河畔的，河边confident[ˈkɒnfɪdənt]确信的；自信的imitating[ˈɪmɪˌteɪt]模仿；仿造好了，今天故事“猴子和渔民”就到这里了，故事比较简短，但故事情节非常有趣。有时候过于相信自己的能力，可能会遍体鳞伤。",
            "这个幼儿英语故事比较简短，但故事情节非常有趣。快跟小编一起来读读吧：The Frog and the CowBaby frogs went on a picnic in the woods. Getting out of the pond for the first time, they sang merrily.Then, they found a cow grazing in a field. “Oh, my! What is that?” “It is huge!” All of them wondered what kind of animal it was. “Let's ask Daddy.”They returned home in a hurry and shouted, “Daddy, we saw a strange animal.” “What kind of animal was it?”“It had large horns on its head and its body was way bigger than you. Even if we all add up our power, we can not defeat that animal.“The father was curious what the animal looked like. “Really? Was it bigger than my stomach?”“Yes. Much bigger than that!”The father frog blew up his stomach largely, “Well, now, I'm as big as the animal, right?” “No, you are as big as the animal's heel.”The father puffed himself up deeply and blew up his stomach enormously.“How about now? Am I as big as the animal, huh?" "No, not even. Thinking he could not be outdone, the father frog puffed up his stomach even more.The father frog's stomach was blown up as big as he could get. Right at that very moment, the father frog's stomach burst with a bang.中文：小青蛙们在树林里野餐。这是他们第一次从池塘里出来，他们正在愉快地唱歌。突然，他们发现了一头正在牧场上吃草的奶牛。“哦，天哪！那是什么？好大啊！”他们都很好奇那究竟是什么动物。“咱们问爸爸吧。”他们匆匆忙忙地回了家，大声喊道：“爸爸，我们看到了一只奇怪的动物。”“什么样的动物啊？”“头上有很大的触角，身体比你大得多。就算我们所有人都加起来，都很难打败它。”父亲对他的描述感到很好奇。“真的吗？它比我的肚子还大吗？”“是啊，可比你的肚子大得多！”父亲使劲鼓起了自己的肚子，“现在呢，现在我和那个动物一样大了，对吧？”“不，你现在也就只有那只动物的脚跟那么大。”父亲气急了，又使劲鼓了股他的肚子。“现在呢？现在我和那动物一样大了吧？”“不，还是小。”父亲认为自己不能认输，于是它又深呼吸了一下，肚子又大了一圈。就这样他不停地吹气，肚子已经达到极限了。就在这一瞬间，青蛙爸爸的肚子砰的词汇学习：woods [wʊdz] 森林wondered [ˈwʌndə] 惊奇；惊奇；惊异，想知道，想弄明白returned [rɪˈtɜːnd] 被送回的；归来的；回国的curious [ˈkjʊərɪəs] 好奇的；奇妙的好了，今天的故事就到这里了，有时候妥协一次未尝不好呢，你说是吗？",
            "这个幼儿英语故事比较简短，但故事情节非常有趣。快来和我一起来读读吧：Once upon a time, the animals living on the ground and those flying in the sky fought against each other. However, a bat could not take part on either side because he was timid and had no courage.When the beasts seemed like winning, the bat went to them and said, “I would like to fight with you.” They believed him.Yet, the bat began to worry, as the birds started to move ahead. So, the bat went to them and begged, “I am on your side because I am winged, too.”They pleasantly accepted the bat. “Sure. Since you have wings, you are on our side.”The fight between the birds and the beasts continued and the bat went back and forth to the winning side.Then one day, peace was made in the woods. The birds and the beasts learned that the bat went hither and thither between them. All the animals determined to expel him. Turned away from both sides, the bat started to live in a dark cave.从前，地上的动物和天上的动物经常打架。然而，蝙蝠无法参加任何一方的队伍，因为他很胆小，缺乏勇气当野兽快要胜利的时候，蝙蝠赶过去说：“我要跟你并肩战斗。”他们相信了蝙蝠。然而，鸟儿们占上风的时候，蝙蝠又开始担心。于是，蝙蝠转而投靠他们恳求道：“我是你们这边，你们看我也有翅膀。”他们愉快地接受了蝙蝠。“当然。既然你有翅膀，你就是我们的战友。”鸟儿与野兽的打斗仍然没有停止，蝙蝠来来回回地投靠每次胜利的一方。一天，树林里终于迎来了和平。鸟和野兽得知蝙蝠在他们中间来回地欺骗。所有的动物都同意驱逐他。两方的队伍都不欢迎他，于是，蝙蝠开始在黑暗的洞穴里生活。词汇学习：Once upon a time 很久很久以前，曾经，从前against [əˈɡɛnst] 违反；反对；对...不利pleasantly [ˈplɛzəntlɪ] 愉快地；和蔼地，亲切地accepted [əkˈsɛptɪd] 公认的好了，今天的故事就讲到这里，与我们的周围人相处时不要像蝙蝠一样欺骗别人哦",
            "这个幼儿英语故事比较简短，但故事情节非常有趣。讲述的是：两个人正在沿着山道走，他们是非常要好的朋友。途中，突然遇到一头大熊，他们吓坏了，四处寻找藏身之处。其中的一个人抢先爬上了树，躲了起来，而另一个我遇到了一只熊，他会被熊吃掉吗？Oncepon a time, two young men were walking along the mountain trail. They were very close friends.But, all of a sudden, a bear showed up. Shocked, the young men were looking for a place to hide. One fellow hid himself by climbing up a tree, but the other one was unable to run away.When the bear pounced upon him, the fellow who could not run away threw himself flat down upon the ground and pretended to be dead. The young man on the ground held his breath and stayed still. The bear, coming up to him, put his muzzle close to the man, and sniffed. “He's dead. I don't eat dead meat.”The bear left the young man along and went away. After the bear was gone, the friend in the tree came down. Wiping away his cold sweat, the friend asked, “What did the bear say to you?“oh, the bear told me”, said the other,“Not to hang out with a friend who runs away when a risky situation occurs.”After hearing him, the young man who climbed up the tree alone felt sorry for his behavior. Friends mean being there for each other even when danger comes.词汇学习：mountain [ˈmaʊntən] 山；山脉；大量unable [ʌnˈeɪbəl] 不能的；无能力的pounced [paʊns] 猛扑，突袭muzzle [ˈmʌzəl] 鼻口部；口套；好了，通过以上的故事告诉了我们：遇到危险时，朋友之间应该互相帮助。",
            "这个大家讲的故事主角是父亲与儿子，一位胆小的父亲担心喜欢打猎的儿子受伤并予以阻止，一天，父亲梦见儿子被狮子追杀，醒来后建了一间木屋并将儿子锁在里面，那么喜欢打猎的儿子如何从木屋中逃出去呢？赶紧从下面的故事中找找答案吧。Once upon a time, there lived a very timid-minded father in a town. He was always worried that his son might get hurt. The son was brave and loved hunting, but his father prevented his son from hunting everyday.The father brought pictures of animals to his son's room so that the son would not get bored. The father even stuck a picture of a lion on the wooden wall. However, the son felt stuffy about just staying home.One day, the son vented his anger on the picture of a lion. “You bastard! I cannot go outside because of you! Why did you appear in my father's dream and torture me?”The son hit the picture with his fist.Right then, the wooden wall broke down and a thorn got stuck in his hand. The son tried to take it out, but it did not come out easily. Due to the thorn, the wound enlarged and the inflammation worsened.After a few days, the young son died from the wound. The father who tried to shut his child in lost his child because of his actions.词汇学习Once upon a time很久很久以前，曾经，从前wooden house木屋好了，今天的故事“胆小的父亲”就到这里了，故事比较简短，但故事情节非常有趣。大家是不是对英文故事及英语学习有了更多的积累了呢？喜欢就赶快收藏起来吧~",
            "这个大家讲的故事主角是狮子，一个狮子在森林里安静的睡觉，一只老鼠沿着他的身体爬了上去，在狮子头顶上玩的特别开心，当狮子醒来后发生了什么事情？它会和老鼠打架吗？从下面的故事中找找答案吧。The ray of the warm sunlight told us that it was spring. A lion was sleeping peacefully in the forest.While the lion was fast asleep, a mouse went on top of the lion. The bold mouse played happily on top of the lion. “Yuppie! This is really fun.”The mouse ran around thumping and stomping here and ther.The lion was not able to sleep with all the racket. The lion knew that there was someone on top of him. So, the lion made a surprise attack and rolled on the ground.And the mouse fell over. When the lion saw the mouse he was relieved and said, “Whew! It was only a mouse.”However, far away a fox had seen the scene. The fox laughed mockingly to the lion and said, “You're as big as a mountain and you're afraid of the mouse. You're a coward!” The fox kept making fun of the Lion.Finally the lion spoke, “I wasn't afraid of the mouse. I was only shocked to find a bold enough animal not afraid to run around on top of a lion.” When the fox heard this he quietly left.",
            "这是一篇适合小朋友们学习的英语故事：Too Soft on CrimeNo one knows for sure, but some experts estimate that half of the crimes committed in the US go unreported. Half of those reported never result in the criminal being found. Half of those in which the criminal is found never result in convictions. Half of the convictions result in reduced or full sentences. Half of the full sentences eventually become reduced sentences because of “good behavior” or overcrowded prisons that result in early releases.“The problem,” said Wyatt Earp, a retired police officer, “is that punishment is not swift enough or severe enough. All they get is a slap on the wrist. Too many judges are soft on criminals. We need to change the law so that there is an eye for an eye, and a tooth for a tooth. Even criminals understand physical pain.“If I were president, I would do many things to teach these punks a lesson. Prisons would have no heat and no air-conditioning. Let the jerks freeze in the winter and bake in the summer. They would get one peanut butter and jelly sandwich for breakfast, for lunch, and for dinner. This way we don’t have to worry about prisoners using utensils to injure guards or other inmates, or dig out of prison. And no crunchy or organic peanut butter either—only the cheap stuff. Their only beverage would be water—no soda, milk, coffee, or tea. And no fancy bottled water, either. Their water would be straight from the faucet.”",
            "A woman is standing at a bus stop at noon. A van pulls up. A young man hops out of the van, grabs the woman’s purse, gets back into the van, and it drives off.An elderly man is standing on the sidewalk in front of his home at 10:30 p.m. He is admiring the full moon. A car pulls up right in front of him and stops. Two men get out. One man punches the old man in the mouth. The other man takes the man’s wallet out of his pants. They get back into their car and drive off.A woman puts her laptop and purse into her car in her driveway at 3:15 p.m. She starts the car, and then remembers that she forgot to turn off the TV. She goes back into her house, turns off the TV, and comes back to her car. Her purse and her laptop are gone.The department of transportation built an elevated freeway on top of the 110 freeway in Los Angeles. The new freeway is supported by more than 100 thick concrete columns. Since the freeway was built, each column has been tagged with graffiti and repainted at least ten times.Late one night, someone managed to raise a heavy metal shopping cart to the top of a flagpole outside a supermarket. The next morning, a 56-year-old supermarket worker hooked up the US flag and started to raise it by pulling on the rope. A second later, the cart crashed down on her. She was permanently paralyzed. When released from the hospital, she told a TV reporter that she forgave the culprit. “Please don’t do this again,” she said. “You might kill someone, and that would be terrible.” A police spokesman admitted that they might not ever find the “prankster.”",
            "这个故事的主角是父亲与儿子，一位胆小的父亲担心喜欢打猎的儿子受伤并予以阻止，一天，父亲梦见儿子被狮子追杀，醒来后建了一间木屋并将儿子锁在里面，那么喜欢打猎的儿子如何从木屋中逃出去呢？赶紧从下面的故事中找找答案吧。Once upon a time, there lived a very timid-minded father in a town. He was always worried that his son might get hurt. The son was brave and loved hunting, but his father prevented his son from hunting everyday.One night, the father dreamed of his son being pursued by a lion. After he woke up, he thought, 'I should not leave things like this.' The father built a strong wooden house for his son because he believed his son would not be in danger if he locked his son in the house.The father brought pictures of animals to his son's room so that the son would not get bored. The father even stuck a picture of a lion on the wooden wall. However, the son felt stuffy about just staying home.One day, the son vented his anger on the picture of a lion. “You bastard! I cannot go outside because of you! Why did you appear in my father's dream and torture me?” The son hit the picture with his fist.Right then, the wooden wall broke down and a thorn got stuck in his hand. The son tried to take it out, but it did not come out easily. Due to the thorn, the wound enlarged and the inflammation worsened.After a few days, the young son died from the wound. The father who tried to shut his child in lost his child because of his actions.词汇学习：Once upon a time很久很久以前，曾经，从前wooden house木屋好了，今天的故事“胆小的父亲”就到这里了，故事比较简短，但故事情节非常有趣。大家是不是对英文故事及英语学习有了更多的积累了呢？喜欢就赶快收藏起来吧~",
            "下面一起来看看这篇童话故事：风和太阳。One day the wind said to the sun, “Look at that man walking along the road. I can get his cloak off more quickly than you can.”“We will see about that,” said the sun. “I will let you try first.”“We will see about that,” said the sun. “I will let you try first.”So the wind tried to make the man take off his cloak. He blew and blew, but the man only pulled his cloak more closely around himself.“I give up,” said the wind at last. “I cannot get his cloak off.” Then the sun tried. He shone as hard as he could. The man soon became hot and took off his cloak.有一天风跟太阳说: “看看那个沿着路上走的人.我可以比你快让他把披风脱下来.“我们等着看吧,”太阳说, “我让你先试.因此风尝试让那个人把披风脱下来.他用力地吹,可是那个人把披风拉得更紧.“我放弃了,”风最后说, “我无法让他把披风脱下来.”然后由太阳试试看.他尽可能地晒他.不久,那个人很热就把披风脱下来了.词汇学习: give up放弃; 投降; 把…让给; 戒除at last终于; 卒; 结果; 算是took off脱掉; 开始; 起飞好了，以上就是关于“英语童话故事：风和太阳”的介绍。大家还知道哪些英语童话故事呢？在日常枯燥的英语学习过程中大家可以多读读英语童话故事，来培养自己的英语兴趣，增加对单词，句子的记忆与理解，当然，大家要是喜欢这则故事，可分享给更多的人哦。最后，希望以上的内容能给大家的英语学习有所帮助。One day the staff members of a zoo called a meeting to discuss the problem--how to deal with the kangaroos that were found out of the cage. They came to the conclusion that the cage was placed too low and decided to raise it from one to two meters high. But the next day the kangaroos were still at large and they again raised the cage to three meters.Quite beyond their expectation the next morning they saw the kangaroos still free to go about. They were alarmed and determined to go to all the length by raising the cage to the height of ten meters.Later a giraffe, while chatting with some kangaroos, asked them, “Do you think they will go on raising your cage?”“Hard to say,” said a kangaroo, “if they continue forgetting to fasten the cage door.”有一天，动物园的管理员们发现袋鼠从笼子里跑出来了， 于是开会讨论，一致认为是笼子的高度过低，所以他们决定将笼子的高度由原来的1米加高到2米。结果第二天他们发现，袋鼠还是跑到外面来，所以他们又决定再将高度加高到3米。没想到隔天居然又看到袋鼠全跑到外面，于是管理 员们大为紧张，决定一不做二不休，将笼子的高度加高到10米。一天，长颈鹿和几只袋鼠在闲聊，“你们看，这些人 会不会再继续加高你们的笼子?”长颈鹿问。“很难说。”袋鼠说，“如果他们再继续忘记关门的话!”词汇学习：staff members职工，工作人员a meeting会议好了，以上就是关于“英语童话故事：袋鼠与笼子”的介绍。大家还知道哪些英语童话故事呢？在日常枯燥的英语学习过程中大家可以多读读英语童话故事，来培养自己的英语兴趣，增加对单词，句子的记忆与理解，当然，大家要是喜欢这则故事，可分享给更多的人哦。最后，希望以上的内容能给大家的英语学习有所帮助。",
            "下面一起来看看这篇童话故事：埃杰克斯。Ajax was a man of giant stature,daring but slow.When the Trojan War was about to break out he led his forces from Salamis to join the Greek army at Aulis.As one of the trustiest champions of the Greek cause,he was given thejob of guarding one end of the Greek camp near Troy.He was noted in the battlefield for his bravery and courage.After Achilles' death he became one of the two hot contestants for the dead hero's shield and armour,the other being Odysseus.When the weapons were finally judged to his rival,Ajax went mad for grief.Unable to get over the hardships,he took his own life.When,in order to seek the advice of,Odysseus came to visit the lower world,the shade of Ajax frowned uponhim.In the lower world Ajax chose to be a lion,guided clearly by the bitter recollection of his former life.埃杰克斯是位身材魁梧、骁勇善战、但头脑迟钝的人。当特洛伊战争即将爆发时,他率领军队从萨拉米斯到达奥尔墨斯加入了希腊军队。作为一名为希腊事业奋斗的最可信赖的斗士,他被派去保卫靠近特洛伊的希腊军营边界。战场上,他因作战勇猛而出名。阿基里斯死后,他成为两个最有可能获得阿基里斯的盾甲的有力竞争对手之一。另一名对手是奥德修斯。最后，他的对手胜利了，并得到了盾甲。埃杰克斯悲伤至极,无法自拔,最终结束了自己的生命。奥德修斯为了得到盲人底比斯的忠告而来到阴间;埃杰克斯的幽灵冲着他直皱眉头。在阴间,由于受到前世痛苦记忆的折磨,埃杰克斯选择了做一头狮子。词汇学习：in order to为了…​Ajax埃杰克斯Trojan War 特洛伊战争好了，以上就是关于“英语童话故事：埃杰克斯”的介绍。大家还知道哪些英语童话故事呢？在日常枯燥的英语学习过程中大家可以多读读英语童话故事，来培养自己的英语兴趣，增加对单词，句子的记忆与理解，当然，大家要是喜欢这则故事，可分享给更多的人哦。最后，希望以上的内容能给大家的英语学习有所帮助。",
            "下面一起来看看这篇童话故事：阿波罗Among the crowd of Olympian gods the one most widely admired was Apollo.He was the son of Zeus and Let to.According to Greek mythology,Leto was driven by Hera from land to land at last Poseidon took Pity on her and brought the island of Delos out of water for her to live on.There she gave birth to the twins ,Apollo and Artemis.Apollo was me sun-god.He wore a purple robe.He usually sat in his bright eastern palace early in the morning and madeready to start his daily journey across the sky.During the day hed rove his carriage of gold and ivory , and brought light, life and love to the great world below. Iate in the afternoon he came to the end of his journey in the far western sea and got on his golden boat to return to his eastern home.Apollo was the god of music and poetry.He could stir up all feelings.These feelings are expressed in lofty songs.With his lyre of gold and the sweet accents of his godlike voice heled the choir of the Muses at Olympus.The pleasant music from his lyre was so exciting that stones marched into their places in rhythmic time and of their own will when he helped Poseidonbuild up the walls of Troy.On one occasion,invited to a contest by the human musician Marsyas,he won and then flayed him to death for his pride.On another occasion,he lost out toPan at a musical contest and turned the ears of the judge,King Midas,into those of an ass.His son,Orpheus,took over such skill from the father that his lyre moved man and animals alike.Apollo stood for youthful and manly beauty.His goldenhair,stately manner and air all combined to make him the admiration of the world.A beautiful girl,by the name of Clytle,was so fond of his beauty and glory that from dawn to dusk she knelt on the ground,her hands outstretched towards the sungod,and her eyes looked at his golden wheeled carriage racing across the blue sky.Though her love was not returned,she had never changed her mind about Apollo.The gods were moved at the sad sight,and changed her into a sunflower.在众多的奥林波斯山神中，主神宙斯和雷托之子阿波罗最受推崇。据希腊神话记载,雷托被天后赫拉驱赶得四处流浪。最终是海神波塞冬怜悯她并从海中捞起提落岛让她居住。在岛上,她生了孪生儿子阿波罗和阿尔特弥斯。阿波罗是太阳神。清晨他身着紫色袍,坐在那明亮的东方宫殿,准备开始每日穿越天空的旅行。白天,他驾着用金子和象牙制成的战车,给广阔无垠的大地带来光明、生命和仁爱。黄昏时分,他在遥远的西海结束了旅行,然后就乘上金船返回东方的家中。阿波罗是音乐神和诗神。他可唤起人们倾注于圣歌中的各种情感。在奥林波斯山上,他手拿金质里拉,用悦耳的音调指挥缪斯的合唱。当他帮助波塞冬建造特洛伊城墙时,里拉奏出的音乐如此动听,以致石头有节奏地、自动地各就其位。有一次他接受凡人音乐家马斯亚斯的挑战参加一次竞赛。战胜对方后,他将对手剥皮致死以惩罚他的狂妄自大。在另外一次音乐比赛中,因输给了潘神,他就将裁判迈尔斯国王的耳朵变成了驴耳朵。阿波罗的儿子俄耳甫斯继承了父亲这方面的才能。他的竖琴使人与动物皆受感动。阿波罗象征着青春和男子汉的美。金色的头发、庄重的举止、容光焕发的神态,这些足以使他受到世人的青睐。一位名叫克里提的美丽少女迷恋于他的英俊潇洒,跪在地上,从黎明到黄昏,双手伸向太阳神。她凝视着那辆金质马车在蔚蓝的天空驰骋。虽然她的爱并未得到回报,但她对阿波罗的痴情却从未改变。目睹这悲哀的场面,众神深受感动,将她变成了一株向日葵。",
            "夏天最爽的就在于吃西瓜了，不但颜色鲜艳清爽，味道甘甜，更重要的是冰凉解暑。所以大家在夏天都爱吃西瓜，连猪妈妈和她的儿子都不例外。这天，太阳光火辣辣地照着大地，猪妈妈让小噜噜去地里搬西瓜回来解解渴，小噜噜该怎么把西瓜搬回家，猪妈妈会吃到搬回来的西瓜吗？In spring, the mother pig took the little pig LuLu to the foot of the mountain. They planted some watermelon.When summer came, there were many big round watermelons in the field.One day, the sun was burning like a fire, it was terribly hot on the ground. The mother pig said to the little pig:“Lulu, go to the field to pick a watermelon back,ok?” Lulu said happily:“Ok! No problem.”Then he ran to the watermelon field. When he got to the field, he was happy to find so many big green watermelons. He chose one of the biggest watermelon and picked it from the vine. Then he held it with his hands trying to lift is on his shoulder to carry it home.“Wow!It is so heavy!” Lulu tried several times, but he failed. And he was socked with sweat. He wiped his sweat off and decided to have a rest.Suddenly he saw the monkey Pipi. He was playing with a hoop. Lulu patted his head and said:“I’ve got it.” He thought,the round hoop can roll, the watermelon round too,then it can roll too.He then put the big melon on the ground and rolled it forward quickly.“At last he got home with the watermelon.The mother pig knew the story, she exclaimed:“My child, you are really clever!”春天的时候，猪妈妈带着小猪噜噜，在山坡下种了一大片西瓜。到了夏天，西瓜地里结满了又圆又大的西瓜。有一天，太阳光火辣辣地照着大地，天啊，可热了。猪妈妈对小猪说：“噜噜，你到咱们的地里摘个大西瓜回来解解渴吧！”小猪噜噜高兴地说：“好吧！”说完就往西瓜地里跑。到了地里一看。呵，到处躺着大西瓜，水灵灵的，真惹人喜爱！噜噜挑了个最大的摘了下来。它双手搂着西瓜，想抱起来放在肩上扛回家。“哟，好重呀！”噜噜试着抱了几次都没有抱起来，还累得满头大汗。 它直起身来，擦了擦脸上的汗水想休息一下，再去试试抱西瓜。突然，它看到小猴皮皮在山下边的马路上滚铁环玩呢。小猪噜噜一拍后脑勺高兴地说：“有了，我有办法了。”什么办法呢？小猪噜噜心想：铁环是圆的，可以滚动。西瓜也是圆的，不也可以滚动吗？想到这儿啊，小猪噜噜顾不上休息，把大西瓜放在地上。咕噜噜，咕噜噜地向前滚，一直把西瓜滚到家里猪妈妈看到小猪噜噜把又圆又大的西瓜搬回家，夸奖噜噜是个爱动脑筋的猪娃娃！",
            "A tiger is hungry, he is looking for food. He sees a frog in front of him. “Ha ha! A frog! My dinner!” so he rushes at the frog.Behind the tiger, there is a tortoise. The little tortoise sees it; he bites the tiger’s tail.“Ouch!” cries the tiger and he looks back. The frog hears the voice and jumps into water. “Thank you, little tortoise.”says the frog.But the tiger is very angry. “Bother it! I’ll throw you to the sky!”“Thank you, I like flying in the sky,” says the tortoise.The tiger stops, “I will throw you into the river.”“Oh,no! I can’t swim; I will die if you throw me into the water.” The tiger threw the tortoise into thewater quickly.“Thank you, Mr. Tiger. Bye-bye.” The tortoise and the frog swim away together.“Thank you, Mr. Tiger. Bye-bye.” The tortoise and the frog swim away together.",
            "It was the first day of class. Two of her new ESL classmates wanted to know where Tara was from. They were both from Iraq. Because Tara looked Iraqi, one of the women asked Tara, in English, if she was from Iraq. Tara replied, No, I'mnot. Then the women took turns asking Tara if she was from Iran, or Syria, or Jordan. To each question, Tara responded with a simple no. Laughing, one woman said to the other, She's not from anywhere! The two desks, talking to each other in Arabic.The next day, the teacher divided the students into groups of four. The students in each group asked introductory questions of each other. A student in Tara s group asked her, Where are you from?Tara answered that she was from Iraq. The two women who had questioned Tara the day before were sonly a few feet away. Both of them heard Tara  s response.Aha! they both exclaimed. “You ARE from Iraq!” Tara smiled and said yes. Then she apologized to both of them for lying the day before. She explained that she had not wanted to get into an Arabic conversation with them. It had been her experience that many ESL students continued to speak their native language in ESL class, and Tara had not come to ESL class to practice her Arabic. In her opinion, ESL students should try to speak English only.“I agree,“said Rose.“Youre 100 percent right,“ agreed Jennifer. “Rose and I must stop speaking Arabic to each other. Right, Rose?“Rose nodded, and then said something in Arabic. All three women laughedOver the next four months, Tara became friendly with both women, although she never spoke a word of Arabic to them during class or break. ",
            "I have a lovely dog named Bobby.He looks pretty with short legs,big ears and short tail.He is my gofriend and he is also easy to take care of.I walk him at least twice a day,feed him and spend time with him.He also gives his love to me in return.He is always there to lick me and lie on me.I like playing with him.I think he can tell when I am happy,sad,angry or troubled.Sometimes he can be noisy and run around the room.In a word,he is not only my dog,but also my friend.I love him. He can roll on the floor. He can play balls with me. He can look after my house when I am out. Bobby is very clever. But sometimes he isn’t.One day Bobby runs away. He is out for three days. After he comes back, I tie him to a tree and give him some food. Bobby begins to eat. But then he stops. He sees a fox. The fox is looking at his food. Bobby barks and barks. He wants to catch the fox. But he can’t. The fox runs round the tree. Bobby runs after the fox. So the rope goes ground the tree. Of course Bobby can’t run. Quickly he eats up the food and runs away.",
            "A man once had four sons who never stopped quarrelling with one another. He was always telling them how much easier life would be if they worked together but they took absolutely no notice of him. One day he decided to show them what he meant.He called all the sons together and put a tightly tied bundle of sticks on the floor in front of theCan you break that ?  he asked the youngest son. The boy put his knee on the bundle but though he pressed and pulled with his arms he could not bend the wood.The father asked each son in turn to try to break the bundle, but none of them could do it . Then he untied the string and scattered the sticks. Now try,  he said . The boys broke the sticks easily in their hands.Do you see what I mean ? asked the father. if only you stand together no one can hurt you . If you all disagree the whole time and insist on going your separate ways, the first enemy you meet will be able to destroy you. “ United we stand divided we fall.",
            "A dog is very thirsty. But he only sees some empty pails. There is no water in them. The dog goes on looking for water. He comes to a small house. There is a girl in it. The girl goes out with a pail. “She goes to a well,” the dog thinks and follows her. The dog is right. The girl comes to a well and puts down the pail, and the pail is full of water, there the girl goes back to her house.“ Water! Great!” the dog says and runs to the well. He jumps into the well without thought.The water is good. The dog is happy and drinks much. But he can’t jump out of the well. He waits and waits. But no one comes. “I’m hungry now. I must go out,” he thinks.At the time a thirsty goat comes to the well. He looks at the water and the dog. “Is the water good?” the goat asks. “ Of course. Come down,” the dog says. Then the goat jumps into the well, too. Then dog is happy. He jumps on the goat’s back and jumps out of the well.The dog has a look at the goat and says, “Goodbye!” Then he leaves.",
            "I had another bad dream,“ she told her fiancé. It was about you again. You and your ex-girlfriend were kissing. I yelled at you to stop it. You looked right at me, and then you laughed at me! She laughed, too. Then you both went back to kissing. I tried not to watch, but when I covered my eyes, something pulled my hands away. I tried to leave, but my feet were glued to the ground. Finally, I woke up. Of course, it was very difficult to get back to sleep. I had to drive home from Las Vegas this morning. It's a wonder I didn't crash 50 times. Instead of seeing traffic in front of me, all I saw was you and her. I can't take any more dreams like this. We're going to have to break up. We can be friends, but just friends. That way, I won't be jealous anymore, and I won't have these bad dreams anymore.""Why didn't you call me up and tell me about your dream? he asked. They say that the more you talk about bad dreams, the sooner you'll stop having them.She disagreed. She thought that the only solution was to break up and be just friends. She loved him, but these dreams had become so frequent that she was actually afraid to go to sleep. She was losing weight and having stomachaches from the stress.He didn't know what to do. He wanted her to have pleasant dreams. He wanted her to have a life without stress. He wanted her to be his wife. This was it, she repeated; if she had just one more bad dream, they were through. He squeezed her hand, but said nothing.","I had another bad dream, she told her fiancé. It was about you again. You and your ex-girlfriend were kissing. I yelled at you to stop it. You looked right at me, and then you laughed at me! She laughed, too. Then you both went back to kissing. I tried not to watch, but when I covered my eyes, something pulled my hands away. I tried to leave, but my feet were glued to the ground. Finally, I woke up. Of course, it was very difficult to get back to sleep.“I had to drive home from Las Vegas this morning. It's a wonder I didn't crash 50 times. Instead of seeing traffic in front of me, all I saw was you and her. I can't take any more dreams like this. We're going to have to break up. We can be friends, but just friends. That way, I won't be jealous anymore, and I won't have these bad dreams anymore.“Why didn't you call me up and tell me about your dream?“ he asked. “They say that the more you talk about bad dreams, the sooner you'll stop having them.“She disagreed. She thought that the only solution was to break up and be just friends. She loved him, but these dreams had become so frequent that she was actually afraid to go to sleep. She was losing weight and having stomachaches from the stress.He didn't know what to do. He wanted her to have pleasant dreams. He wanted her to have a life without stress. He wanted her to be his wife. This was it, she repeated; if she had just one more bad dream, they were through. He squeezed her hand, but said nothing.",
            "As a young man, Al was a skilled artist, a potter with a wife and two fine sons. One night, his older son developed a severe stomachache. Thinking it was only some common intestinal(肠的) disorder, neither Al nor his wife took the condition very seriously . But the boy died suddenly that night.Knowing the death could have been avoided if he had only realized the seriousness of the situation, he always felt he was guilty. To make matters worse, his wife left him a short time later, leaving him alone with his six-year-old younger son. The hurt and pain of the two situations were more than Al could stand, and he turned to alcohol for help. In time Al became an alcoholic.As the alcoholism progressed, AL began to lose everything he possessed -- his land, house, etc. Finally Al died alone in a small bar. Hearing of Al's death, I thought, “What a totally wasted life! What a complete failure!As the alcoholism progressed, AL began to lose everything he possessed -- his land, house, etc. Finally Al died alone in a small bar. Hearing of Al's death, I thought, “What a totally wasted life! What a complete failure! As time went by , I began to revalue my earlier rough judgement . I knew Al's now adult son, Ernie. He is one of the kindest, most caring , most loving men I have ever known. I saw the love between Ernie and his children, thinking that kindness and caring had to come from somewhereI hadn't heard Ernie talked much about his father. One day, I worked up my courage to ask him what on earth his father had done so that he became such a special person. Ernie said quietly, “As a child until I left home at 18, Al came into my room every night, gave me a kiss and said, “love you, so .Tears came to my eyes as I realized what I had been a fool to judge Al as a failure. He had not left any material possessions behind. But he had been a kind loving father, and left behind his best lov",
            "There was once a bridge which spanned a large river. During most of the day the bridge sat with its length running up and down the river paralleled with the banks, allowing ships to pass thru freely on both sides of the bridge. But at certain times each day, a train would come along and the bridge would be turned sideways across the river, allowing a train to cross it.A switchman sat in a small shack on one side of the river where he operated the controls to turn the bridge and lock it into place as the train crossed. One evening as the switchman was waiting for the last train of the day to come, he looked off into the distance thru the dimming twilight and caught sight of the trainlights. He stepped to the control and waited until the train was within a prescribed distance when he was to turn the bridge. He turned the bridge into position, but, to his horror, he found the locking control did not work. If the bridge was not securely in position it would wobble back and forth at the ends when the train came onto it, causing the train to jump the track and go crashing into the river. This would be a passenger train with many people aboard. He left the bridge turned across the river, and hurried across the bridge to the other side of the river wher He would have to hold the lever back firmly as the train crossed. He could hear the rumble of the train now, and he took hold of the lever and leaned backward to apply his weight to it, locking the bridge. He kept applying the pressure to keep the mechanism locked. Many lives depended on this man's strength.Then, coming across the bridge from the direction of his control shack, he heard a sound that made his blood run cold. “Daddy, where are you?” His four-year-old son was crossing the bridge to look for him. His first impulse was to cry out to the child, “Run! Run!” But the train was too close; the tiny legs would never make it across the bridge in time. The man almost left his lever to run and snatch up his son and carry him to safety. But he realized that he could not get back to the lever. Either the people on the train or his little son must die. He took a moment to make his decision.The train sped safely and swiftly on its way, and no one aboard was even aware of the tiny broken body thrown mercilessly into the river by the onrushing train. Nor were they aware of the pitiful figure of the sobbing man, still clinging tightly to the locking lever long after the train had passed. They did not see him walking home more slowly than he had ever walked: to tell his wife how their son had brutally died.Now if you comprehend the emotions which went this man's heart, you can begin to understand the feelings of our Father in Heaven when He sacrificed His Son to bridge the gap between us and eternal life. Can there be any wonder that He caused the earth to tremble and the skies to darken when His Son died? How does He feel when we speed along thru life without giving a thought to what was done for us thru Jesus Christ?",
            "A mouse once took a bite out of a bull's tail as he lay dozing. The bull jumped up in a rage and, with his head low to the ground, chased the mouse right across the yard. The mouse was too quick for him, however, and slipped easily into a hole in the wall.The bull charged the wall furiously again and again, but although he bruised his head and chipped his horns, the mouse stayed safely inside his hole. After a time the bull gave up and sank down to rest again.As soon as the bull was asleep, the little mouse crept to the mouth of the hole, pattered across the yard, bit the bull again -- this time on the nose -- and rushed back to safety. As the bull roared helplessly the mouse squeaked:“It's not always the big people who come off best. Sometimes the small ones win, you know.",
            "There is a naughty boy in a village. He likes telling lies. One day he wants to make fun of the farmers. So he shouts, “Wolf! Wolf! Wolf is coming!” The kind farmers are working in the field. They hear the shout, and hurry to help the boy. But when get there, the boy says: “There isn’t a wolf. I’m joking. The farers are angry and go back to their field. After a while the biy shouts again, “Wolf! Wolf! Wolf is coming!” And the farmers come and are cheated again. The boy laughs and laughs. They say, “You tell lies. We will not believe you.” Later a wolf really comes. The boy is very scared. “Wolf! Wolf! Wolf is coming!” the boy shouts and shouts. “Help! Help!” But no one comes. And wolf eats the naughty['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', ''],
            ['', '']
        ]
        # idiom data
        self.idiom_story = { #145
            '滥竽充数': ['滥竽充数这则成语的滥是失实，与真实不符，引申为蒙混的意思；竽是一种簧管乐器；充数是凑数。指没有真才实学的人混在行家里充数，或是以次充好，有时也用作自谦之辞。这个成语来源于《韩非子.内储说上》，齐宣王使人吹竿，必三百人。南郭处士请为王吹竽，宣王说之，廪食以数百人。宣王死，潜王立，好一一听之，处士逃。战国时期，齐宣王非常喜欢听人吹竽，而且喜欢许多人一起合奏给他听，所以齐宣王派人到处搜罗能吹善奏的乐工，组成了一支三百人的吹竽乐队。而那些被挑选入宫的乐师，受到了特别优厚的待遇。当时，有一个游手好闲、不务正业的浪荡子弟，名叫南郭。他听说齐宣王有这种嗜好，就一心想混进那个乐队，便设法求见宣王，向他吹嘘自己是一名了不起的乐师，博得了宣王的欢心，把他编入了吹竽的乐师班里。可笑的是，这位南郭先生根本不会吹竽。每当乐队给齐宣王吹奏的时候，他就混在队伍里，学着别的乐工的样子，摇头晃脑，东摇西摆，装模做样地在那儿吹奏。因为他学得维妙维肖，又由于是几百人在一起吹奏，齐宣王也听不出谁会谁不会。就这样，南郭混了好几年，不但没有露出一丝破绽，而且还和别的乐工一样领到一份优厚的赏赐，过着舒适的生活。后来，齐宣王死了，他儿子齐潜王继位，潜王同样爱听吹竽。只有一点不同，他不喜欢合奏，而喜欢乐师门一个个单独吹给他听。南郭先生听到这个消息后，吓得浑身冒汗，整天提心吊胆的。心想，这回要露出马脚来了，丢饭碗是小事，要是落个欺君犯上的罪名，连脑袋也保不住了。所以，趁潜王还没叫他演奏，就赶紧溜走了。 ', ''],
            '画蛇添足': ['战国时楚国有位管祠堂的人，在祭祀后把酒分给底下办事的人，但酒不够分，于是他们想出一个办法来：大家在地上画蛇，画得最快的人就可以喝酒。其中一人画得最快，正打算拿酒来喝，因见其它人还未画好，他就再为蛇添上脚，此时另一人刚好画好了，便从他的手上把酒抢过来，并说：“蛇本来没有脚，你为甚么要为它添上脚呢？”说完就把酒喝掉了。', ''],
            '守株待兔': ['春秋时代有位宋国的农夫，他每天早上很早就到田里工作，一直到太阳下山才收拾农具准备回家。有一天，农夫正在田里辛苦的工作，突然却远远跑来一只兔子。这只兔子跑得又急又快，一个不小心，兔子撞上稻田旁边的大树，这一撞，撞断了兔子的颈部，兔子当场倒地死亡。一旁的农夫看到之后，急忙跑上前将死了的兔子一手抓起，然后很开心的收拾农具准备回家把这只兔子煮来吃。农夫心想，天底下既然有这么好的事，自己又何必每天辛苦的耕田？从此以后，他整天守在大树旁，希望能再等到不小心撞死的兔子。可是许多天过去了，他都没等到撞死在大树下的兔子，反而因为他不处理农田的事，因此田里长满了杂草，一天比一天更荒芜。', ''],
            '刻舟求剑': ['这个成语来源于《吕氏春秋.察今》，楚人有涉江者，其剑自舟中坠于水，遽契其舟曰：是吾剑之所从坠。舟止，从其所契者入水求之。战国时，楚国有个人坐船渡江。船到江心，他一不小心，把随身携带的一把宝剑掉落江中。他赶紧去抓，已经来不及了。船上的人对此感到非常惋惜，但那楚人似乎胸有成竹，马上掏出一把小刀，在船舷上刻上一个记号，并向大家说：这是我宝剑落水的地方，所以我要刻上一个记号。大家都不理解他为什么这样做，也不再去问他。船靠岸后那楚人立即在船上刻记号的地方下水，去捞取掉落的宝剑。捞了半天，不见宝剑的影子。他觉得很奇怪，自言自语说：我的宝剑不就是在这里掉下去吗？我还在这里刻了记号呢，怎么会找不到的呢？至此，船上的人纷纷大笑起来，说：船一直在行进，而你的宝剑却沉入了水底不动，你怎么找得到你的剑呢？其实，剑掉落在江中后，船继续行驶，而宝剑却不会再移动。像他这样去找剑，真是太愚蠢可笑了。《吕氏春秋》的作者也在写完这个故事后评论说这个，刻舟求剑的人是太愚蠢可笑了！', ''],
            '掩耳盗铃': ['从前有一个人，看见人家门口有一口大钟，就想把它偷去。可这钟太重，没法背走，他就取来一个铁锤，想敲碎后一块块偷走。可是还有一个问题，用铁椎砸钟会发出很大的声音，肯定会被人抓做的。他转念一想：钟一响耳朵就能听见，可是如果把耳朵蒙起来，就什么都听不到了！掩耳盗铃：比喻蠢人自己欺骗自己。《吕氏春秋·自知》：有得钟者，欲负而走，则钟大不可负。以椎毁之，钟况然有音。恐人闻之而夺已也，遽掩其耳。', ''],
            '买椟还珠': ['春秋时代，楚国有一个商人，专门卖珠宝的，有一次他到齐国去兜售珠宝，为了生意好，珠宝畅销起见，特地用名贵的木料，造成许多小盒子，把盒子雕刻装饰得非常精致美观，使盒子会发出一种香味，然后把珠宝装在盒子里面。有一个郑国人，看见装宝珠的盒子既精致又美观，问明了价钱后，就买了一个，打开盒子，把里面的宝物拿出来，退还给珠宝商。', ''],
            '自相矛盾': ['战国时楚国有一个卖盾和矛的人，他夸说自己所卖的盾坚固无比，没有东西能把它刺穿；又夸说自己所卖的矛十分锋利，没有东西不被它刺穿。路上有人听见后，忍不住说：“如果用你的矛去刺你的盾，结果会如何？”楚国人立刻瞠目结舌，无法回答他的问题。', ''],
            '亡羊补牢': ['战国七雄之一的楚国，国土比较大，国势比较强，可是传至襄王，宠信佞臣，一意贪图享受，朝政一天比一天紊乱。有一位大臣庄辛，忠心耿耿，看到这种情形，知道楚国已经伏下了严重的危机，十分担忧。有一天就向襄王说：“大王的四周有州侯、夏侯、鄢陵君和寿陵君这四个人，大王一味宠信他们，受了他们包围，整天陶醉在酒里，浪费国帑，不管国家大事，这样下去，恐怕楚国难保了。”襄王听了，很不高兴，就用责备的口吻说：“你喝醉了吧？要不然就是你老糊涂了！你看国跟国之间互不侵扰，国内又太平无事，不知道你为什么说这些不吉祥的话？也许你要变成楚 ', ''],
            '望梅止渴': ['南朝？宋？刘义庆《世说新语？假谲》：有一次曹操带兵在外行军，一时找不到取水的地方，士兵都渴极了，曹操就骗他们说：“前面有个大梅林，梅子又甜又酸，可以解渴。”士兵听了，一个个都流出了口水，暂时止住了口渴。', ''],
            '纸上谈兵': ['赵括从小学习兵法，自以为天下没有人能够与其匹敌。他的父亲赵奢曾经评论说：“打仗是非常危险的事情，而赵括把它说得太容易了，假使将来赵国不任命他为将军，那也就算了，如果一定要拜他为将军，导致赵军大败的人必定是赵括无疑。”后来赵括果然代替廉颇做了大将军，长平一战被秦将白起打败，四十万赵军全部被消灭，赵括自己也战死了。', ''],
            '卧薪尝胆': ['春秋时期，吴王夫差凭着自己国力强大，领兵攻打越国。结果越国战败，越王勾践于是被抓到吴国。吴王为了羞辱越王，因此派他看墓与喂马这些奴仆才做的工作。越王心里虽然很不服气，但仍然极力装出忠心顺从的样子。吴王出门时，他走在前面牵着马；吴王生病时，他在床前尽力照顾，吴王看他这样尽心伺候自己，觉得他对自己非常忠心，最后就允许他返回越国。越王回国后，决心洗刷自己在吴国当囚徒的耻辱。为了告诫自己不要忘记复仇雪恨，他每天睡在坚硬的木柴上，还在门上吊一颗苦胆，吃饭和睡觉前都要品尝一下，为的就是要让自己记住教训。除此之外，他还经常到民间视察民情，替百姓解决问题，让人民安居乐业，同时加强军队的训练。经过十年的艰苦奋斗，越国变得国富兵强，于是越王亲自率领军队进攻吴国，也成功取得胜利，吴王夫差羞愧得在战败后自杀。后来，越国又趁胜进军中原，成为春秋末期的一大强国。 ', ''],
            '四面楚歌': ['项羽和刘邦原来约定以鸿沟（在今河南荣县境贾鲁河）东西边作为界限，互不侵犯。后来刘邦听从张良和陈平的规劝，觉得应该趁项羽衰弱的时候消灭他，就又和韩信、彭越、刘贾会合兵力追击正在向东开往彭城（即今江苏徐州）的项羽部队。终于布置了几层兵力，把项羽紧紧围在垓下（在今安徽灵璧县东南）。这时，项羽手下的兵士已经很少，粮食又没有了。夜里听见四面围住他的军队都唱起楚地的民歌，不禁非常吃惊地说：刘邦已经得到了楚地了吗？为什么他的部队里面楚人这么多呢？说看，心里已丧失了斗志，便从床上爬起来，在营帐里面喝酒，并和他最宠爱的妃子虞姬一同唱歌。唱完，直掉眼泪，在一旁的人也非常难过，都觉得抬不起头来。虞姬自刎于项羽的马前，项羽英雄末路，带了仅剩兵卒至乌江，最终自刎于江边。以后人们就用四面楚歌这个词，形容人们遭受各方面攻击或逼迫，而陷于孤立窘迫的境地。凡是陷于此种境地者，其命运往往是很悲惨的。例如某人因经常与坏人为伍，不事生产，游手好闲，但后来却被那些坏人逼迫得无以为生，而求助于别人时，别人又因他平日行为太坏，绝不同情理睬，这人所处的境地便是四面楚歌。', ''],
            '指鹿为马': ['秦朝二世的时候，宰相赵高掌握了朝政大权。他因为害怕群臣中有人不服，就想了一个主意。有一天上朝时，他牵着一只梅花鹿对二世说：陛下，这是我献的名马，它一天能走一千里，一夜能走八百里。二世听了，大笑说：承相啊，这明明是一只鹿，你却说是马，真是错得太离谱了！赵高说：这确实是一匹马，陛下怎么说是鹿呢？二世觉得纳闷，就让群臣百官来评判。大家心想，说实话会得罪承相，说假话又怕欺骗陛下，就都不出声。这时赵高盯着群臣，指着鹿大声问：大家看，这样身圆腿瘦，耳尖尾粗，不是马是甚么？大家都害怕赵高的势力，知道不说不行，就都说是马，赵高非常得意，二世被弄胡涂了，明明是鹿，怎么大家都说是马呢？他以为自己疯了，从此越来越胡涂，朝政上的事都完全由赵高来操纵。赵高暗中把那些说实话的人杀掉，又派人杀死二世，霸占整个朝廷，最后终于导致秦朝灭亡。', ''],
            '画龙点睛': ['传说古时候有个画家叫张僧繇，他画龙画得特别好。有一次，他在金陵（现在南京）安乐寺的墙壁上画了四条巨龙，那龙画得活灵活现，非常逼真，只是都没有眼睛。人们问张僧繇：“为什么不把眼睛画出来。”他说：“眼睛可不能轻易画呀！一画了，龙就会腾空飞走的！”大家听了，谁也不信，都认为他在说大话。后来，经不起人们一再请求，张僧繇只好答应把龙的眼睛画出来。奇怪的事情果然发生了，他刚刚点出第二条龙的眼睛，突然刮起了大风，顷刻间电闪雷鸣。两条巨龙转动着光芒四射的眼睛冲天而起，腾空而去。围观的人，个个看得目瞪口呆，对张僧繇更佩服了。成语“画龙点睛”就是从这个传说中来的。现在一般用来比喻写作、讲话时，在关键性的地方用上一两句精辟的语言来点明含义，使内容更加生动有力。这种手法也称为“点睛”之笔。', ''],
            '攀龙附凤': ['“攀龙附凤”这则成语的“龙、凤”是形容有权势的人。比喻巴结或投靠有权势的人。这个成语来源于《汉书.叙转下》，午阳鼓刀，滕公厩驺，颖阴商贩，曲周庸夫，攀龙附凤，并乘天衢。西汉的开国皇帝刘邦，出身于一个农民家庭，他的父母连名字都没有。刘邦原名季，意思是“老三”，直到做了皇帝，才改名为邦。刘邦三十岁时，当了秦朝沛县的一个乡村小吏——亭长。他为人豁达大度，胸怀开朗，做事很有气魄，很多人都和他合得来。当地的萧何、樊哙、夏侯婴等，都是他的好朋友。这些人后来都为刘邦建立汉朝出了大力。樊哙是刘邦的同乡，是个杀狗卖狗的。陈胜、吴广发动起义后，沛县县令惊恐万分，打算投起义之机响应陈胜，就派樊哙去召刘邦来相助。不料刘邦带了几百人来时，县令又反悔起来。于是，刘邦说服城里人杀了县令，带领二三千人马誓师起兵。夏侯婴与刘邦也早就有了交情。他原来是县衙里的马夫，每次奉命为过往使者赶车，回来时经过刘邦那里，总要与刘邦闲谈很长时间，直到日落西山才走。后来夏侯婴当了县吏，与刘邦交往更密切了。一天刘邦与他闹着玩，一不小心打伤了他。有人告刘邦身为亭长，动手打人，应当严惩，夏侯婴赶紧为他解释。不料，后来夏侯婴反以伪证罪被捕下狱，坐了一年多班房。后来刘邦在沛县起兵，他和樊哙主动参加，并担任部将。刘邦的势力逐渐发展后，有个名叫灌婴的人又来投奔他。灌婴是睢阳人，本为贩卖丝绸的小商人。此人后来也成为刘邦的心腹，领兵转战各地，立了不少战功。公元前208年，刘邦根据各路起义军开会的决定，带领人马西攻秦都咸阳。第二年初，刘邦大军兵临陈留，把营扎在城郊，当地有个名叫郦食其的小吏前来献计。郦食其对刘邦说，现在您兵不满万人，又缺乏训练，要西攻强秦，如进虎口。不如先攻取陈留，招兵买马，等兵强马壮后再打天下。郦食其还表示，他和陈留县令相好，愿意前去劝降；如县令不降，就把他杀了。刘邦采纳了郦食其的计谋。郦食其连夜进陈留城劝说县令，但那县令不肯起义。于是郦食其半夜割下他的头颅来见刘邦。第二天刘邦攻城时，把那县令的头颅高悬在竹竿上，结果守军开城门投降。在陈留，刘邦补充了大量粮食、武器和兵员。接着郦食其又推荐了他颇有智勇的弟弟郦商，郦商又给刘邦带来了四千人。刘邦就任命他为副将，带领这支队伍西攻开封。后来，刘邦又战胜项羽，在公元前202年即皇帝位，建立了西汉王朝。刘邦当皇帝后大封功臣，樊哙、夏侯婴、灌婴、郦商等人也先后被封为舞阳侯、当汝阴侯、颖阴侯和曲周侯。', ''],
            '叶公好龙': ['春秋时，有位叫叶公的人非常喜欢龙。他家的屋梁上、柱子上和门窗上都雕刻着龙的图案，墙上也绘着龙。传说天上的真龙知道此事后很受感动，专程到叶公家里来，把头从窗口伸进屋子里，把尾巴横在客堂上。叶公看到后，吓得面无血色，魂不附体，抱头就跑。原来他并不是真正喜欢龙。他爱的是假龙，怕的是真龙。这个成语比喻表面上爱好某一事物，实际上并不是真正爱好它，甚至是畏惧它。', ''],
            '精卫填海': ['传说，很久以前，炎帝有个女儿叫女娃，炎帝很喜欢她，经常带她到东海去游泳。女娃非常勇敢，大风大浪从不畏惧。女娃长大后，每天都要自己到东海去游泳。有一天，她不幸被大海淹死了。女娃死后变成了一只鸟，每天从山上衔来石头和草木，投入东海，然后发出“精卫”“精卫”的叫声，好像在呼唤着自己。精卫鸟日复一日，年复一年，顽强不息，坚持不懈，决心要把东海填平。这句成语比喻矢志不移，努力不懈。后人常以“精卫填海”这个成语比喻深仇大恨，立志必报。或比喻不畏艰难险阻，矢志不移的坚毅决心。', ''],
            '开天辟地': ['神话中传说，世上最早时，天地浑然一体。世界像个鸡蛋，天地的开创人盘古就在蛋里。一万八千年后，盘古从蛋里走出来。蛋里淡淡的烟云冉冉上升，变成青天。混浊的沉渣逐渐凝聚，变成大地。天地近在咫尺。盘古弯曲着背把天地撑开。盘古顶开立地一万八千年，终于把天撑高。天地再也不会合在一起，盘古才安然死去。他呼出的气，变成风和云。他留下的声音，变成雷霆。他的眼睛变成太阳和月亮。盘古开创了世界。颂扬开创伟大事业，称开天辟地。', ''],
            '三顾茅庐': ['东汉末年，诸葛亮居住在隆中的茅庐里。谋士徐庶向刘备推荐说：诸葛亮是个奇才。刘备为了请诸亮帮助自己打天下，就同关羽、张飞一起去请他出山。可是诸葛亮不在家，刘备只好留下姓名，怏怏不乐地回去。隔了几天，刘备打听到诸葛亮回来了，又带着关羽、张飞冒着风雪前去。哪知诸葛亮又出门出去了，刘备他们又空走一趟。刘备第三次去隆中，终于见到了诸葛亮。在交谈中，诸葛亮对天下形势作了非常精辟的分析，刘备十分叹服。刘备三顾茅庐，使诸葛亮非常感动，答应出山相助。刘备尊诸葛亮为军师，对关羽、张飞说：我之有孔明，犹鱼之有水也！诸葛亮初出茅庐，就帮刘备打了不少胜仗，为刘备奠定了蜀汉的国基。成语三顾茅庐由此而来', ''],
            '草船借箭': ['“草船借箭”这则成语的意思是运用智谋，凭借他人的人力或财力来达到自己的目的。这个成语来源于《三国演义》，用奇谋孔明借箭。三国时期，曹操率大军想要征服东吴，孙权、刘备联合抗曹。孙权手下有位大将叫周瑜，智勇双全，可是心胸狭窄，很妒忌诸葛亮（字孔明）的才干。因水中交战需要箭，周瑜要诸葛亮在十天内负责赶造十万支箭，哪知诸葛亮只要三天，还愿立下军令状，完不成任务甘受处罚。周瑜想，三天不可能造出十万支箭，正好利用这个机会来除掉诸葛亮。于是他一面叫军匠们不要把造箭的材料准备齐全，另一方面叫大臣鲁肃去探听诸葛亮的虚实。鲁肃见了诸葛亮。诸葛亮说：“这件事要请你帮我的忙。希望你能借给我20只船，每只船上30个军士，船要用青布慢子遮起来，还要一千多个草把子，排在船两边。不过，这事千万不能让周瑜知道。”鲁肃答应了，并按诸葛亮的要求把东西准备齐全。两天过去了，不见一点动静，到第三天四更时候，诸葛亮秘密地请鲁肃一起到船上去，说是一起去取箭。鲁肃很纳闷。诸葛亮吩咐把船用绳索连起来向对岸开去。那天江上大雾迷漫，对面都看不见人。当船靠近曹军水寨时，诸葛亮命船一字儿摆开，叫士兵擂鼓呐喊。曹操以为对方来进攻，又因雾大怕中埋伏，就派六千名弓箭手朝江中放箭，雨点般的箭纷纷射在草把子上。过了一会，诸葛亮又命船掉过头来，让另一面受箭。太阳出来了，雾要散了，诸葛亮令船赶紧往回开。这时船的两边草把子上密密麻麻地插满了箭，每只船上至少五、六千支，总共超过了十万支。鲁肃把借箭的经过告诉周瑜时，周瑜感叹地说：“诸葛亮神机妙算，我不如他。”', ''],
            '草木皆兵': ['这个成语来源于《晋书.苻坚载记》，坚与苻融登城而望王师，见部阵齐整，将士精锐；又北望八公山上草木，皆类人形。公元383年，基本上统一了北方的前秦皇帝苻坚，率领90万兵马，南下攻伐东晋。东晋王朝任命谢石为大将，谢玄为先锋，率领8万精兵迎战。秦军前锋苻融攻占寿阳（今安徽寿县）后，苻竖亲自率领八千名骑兵抵达这座城池。他听信苻融的判断，认为晋兵不堪一击，只要他的后续大军一到，一定可大获全胜。于是，他派一个名叫朱序的人去向谢石劝降。朱序原是东晋官员，他见到谢石后，报告了秦军的布防情况，并建议晋军在前秦后续大军未到达之前袭击洛涧（今安徽淮南东洛河）。谢石听从他的建议，出兵偷袭秦营，结果大胜。晋兵乘胜向寿阳进军。苻坚得知洛涧兵败，晋兵正向寿阳而来，大惊失色，马上和苻融登上寿阳城头，亲自观察淝水对岸晋军动静。当时正是隆冬时节，又是阴天，远远望去，淝水上空灰蒙的一片。仔细看去，那里桅杆林立，战船密布，晋兵持刀执戟，阵容甚为齐整。他不禁暗暗称赞晋兵布防有序，训练有素。接着，苻坚又向北望去。那里横着八公山，山上有八座连绵起伏的峰峦，地势非常险要。晋兵的大本营便驻扎在八公山下。随着一阵西北风呼啸而过，山上晃动的草木，就像无数士兵在运动。苻坚顿时面如土色，惊恐地回过头来对苻融说：晋兵是一支劲敌，怎么能说它是弱兵呢？不久，苻坚中谢玄的计，下令将军队稍向后退，让晋兵渡过淝水决战。结果，秦兵在后退时自相践踏，溃不成军，大败北归。这一战，便是历史上著名的淝水之战，是历史上以少胜多，以弱胜强的著名战例。', ''],
            '破釜沉舟': ['破釜沉舟”这则成语的釜是锅；舟是船。砸破烧饭用的锅子，凿沉船只，比喻拚死一战。这个成语来源于《史记.项羽本纪》，项羽乃悉引兵渡河，皆沉船，破釜甑，烧庐舍，持三日粮，以示士卒必死，无一还心。秦朝末年，秦二世派大将章邯攻打赵国。赵军不敌，退守巨鹿（今河北平乡西南），被秦军团团围住。楚怀王封宋义为上将军，项羽为副将，派他们率军去救援赵国。不料，宋义把兵带到安阳（今山东曹县东南）后，接连46天停滞不进。项羽忍不住，一再要求他赶紧渡江北上，赶到巨鹿，与被围赵军来个里应外合。但宋义另有所谋，想让秦、赵两军打得精疲力竭再进兵，这样便于取胜。他严令军中，不听调遣的人，不管是谁都要杀。与此同时，宋义又邀请宾客，大吃大喝，而士兵和百姓却忍饥挨饿。项羽忍无可忍，进营帐杀了宋义，并声称他勾结齐国反楚，楚王有密令杀他。将士们马上拥戴项羽代理上将军。项羽把杀宋义的事及原因报告了楚怀王，楚怀王只好正式任命他为上将军。项羽杀宋义的事，震惊了楚国，并在各国有了威名。他随即派出两名将军，率2万军队渡河去救巨鹿。在获悉取得小胜并接到增援的请求后，他下令全军渡河救援赵军。项羽在全军渡河之后，采取了一系列果断的行动：把所有的船只凿沉，击破烧饭用的锅子，烧掉宿营的屋子，只携带三天干粮，以此表示决心死战，没有一点后退的打算。这支有进无退的大军到了巨鹿外围，立即包围了秦军。经过9次激战，截断了秦军的补给线。负责围攻巨鹿的两名秦将，一名被活捉，另一名投火自焚。在这之前，来援助赵国的各路诸侯虽然有几路军队在巨鹿附近，但都不敢与秦军交锋。楚军的拚死决战并取得胜利，大大地提高了项羽的声威。从此，项羽率领的军队成了当时反秦力量中最强大的一支武装。后来，“皆沉船，破釜甑”演化为成语“破釜沉舟”，用来比喻拚死一战，决心很大。项羽也成了当时农民起义军的著名领袖人物，并在不久和刘邦的起义军一起，推翻了秦朝的统治。', ''],
            '穷兵黩武': ['东吴后期的名将陆抗，二十岁时就被任命为建武校尉；带领他父亲陆逊留下的部众五千人。公元264年，孙皓当了东吴的国君，三十八岁的陆抗担任镇军大将军。当时，东吴的朝政非常腐败。孙皓荒淫暴虐，宫女有好几千人，还向民间掠夺；又用剥面皮、凿眼睛筹酷刑任意杀人。陆抗对孙皓的所作所为非常不满，多次上疏，劝谏他对外加强防守，对内改善政治，以增强国力。他曾在奏疏中一次陈述当前应做的事达十六件之多。但是，孙皓对他的建议置之不理。公元272年，镇守西陵的吴将步阐投降晋朝。陆抗得知后、立即率军征讨步阐。他知道晋军一定会来接应步阐，', ''],
            '曲高和寡': ['宋玉是楚国伟大诗人屈原的学生。有一天，楚襄王问宋玉：现在不少人对你有意见，你是不是有什么不对的地方？宋玉转弯抹角地回答说：有位歌唱家在我们都城的广场上演唱，唱《下里》《巴人》这些通俗歌曲时，有几千听众跟着唱起来；唱《阳春》《白雪》这类高深歌曲时，能跟着唱的只有几十人；到了唱更高级的歌曲时，跟着唱的只有几个人了。从这里可以看出，曲调越是高深，能跟着一起唱的人就越少。宋玉这段话的意思是说自己品行高超，一般的人不能了解，所以有人说三道四。和（音贺）指跟着别人唱；寡是少的意思。这个成语后来比喻言论、作品很深，能理解的人很少。有时也用来讽刺别人自命不凡。', ''],
            '势如破竹': ['三国末年，晋武帝司马炎灭掉蜀国，夺取魏国政权以后，准备出兵攻打东吴，实现统一全中国的愿望。他召集文武大臣们商量灭大计。多数人认为，吴国还有一定实力，一举消灭它恐怕不易，不如有了足够的准备再说。大将杜预不同意多数人的看法，写了一道奏章给晋武帝。杜预认为，必须趁目前昊国衰弱，忙灭掉它，不然等它有了实力就很难打败它了。司马炎看了杜预的奏章，找自己的最信任的大臣张华征求意见。张华很同意杜预的分析，也劝司马炎快快攻打吴国，以免留下后患。于是司马炎就下了决心，任命杜预作征南大将军。公元279年，晋武帝司马炎调动了二十多万兵马，分成六路水陆并进，攻打吴国，一路战鼓齐鸣，战旗飘扬，战士威武雄壮。第二年就攻占了江陵，斩了吴国一员大将，率领军队乘胜追击。在沅江、湘江以南的吴军听到风声吓破了胆，纷纷打开城门投降。司马炎下令让杜预从小路向吴国国都建业进发。此时，有人担心长江水势暴涨，不如暂收兵等到冬天进攻更有利。杜预坚决反对退兵，他说：“现在趁士气高涨，斗志正旺，取得一个又一个胜利，势如破竹（像用快刀劈竹子一样，劈过几节后竹子就迎刃破裂），一举攻击吴国不会再费多大力气了！”晋朝大军在杜预率领下，直冲向吴都建业，不久就攻占建业灭了吴国。晋武帝统一了全国。 ', ''],
            '室如悬磬': ['有一次，齐孝公出兵去征伐鲁国，鲁君想派人去说服齐国，制止齐国的侵略，但是不知道用什么言词去说服他们，便去问展禽。展禽沉思了一会儿，就说：“我听人说过，处在大国的地位，才可以教导小国；处在小国的地位，却只能服侍大国。惟有这样，才能消除战争。我从来都没有听过，单靠言词就能平息乱事的。假如是个小国，还很自大的话，只会引起大国的恼怒，增加乱事，现在乱事已经开始，不是靠言词就能收到成效的。”展禽说完，就叫乙喜去犒劳齐军，并且对他们说：“我们的君王没有才干，不能好好的管理边界上的事情，以至于劳驾你们，还连累你们的军队露宿在我们的边境上，所以特别派我来犒劳你们所有的兵士。”齐侯说：“你们到现在才恐慌吗？”乙喜说：“敝国现在有德高望重的人辅政，所以并不恐慌。”齐孝公说：“你们室如悬磬，田野里连青草都没得生长，怎么会说不恐慌呢？磬，就是指空无所有的意思。室如悬磬，就是用来比喻穷得什么东西也没有。它和“家徒四壁”都一样，是用来形容极端的贫乏、困苦。', ''],
            '手不释卷': ['三国时，吕蒙是吴国的大将。一次，他点兵3万，用船80余只袭击荆州。水手一律身着白衣，大批精兵埋伏在船舱里。黑夜，船到当阳江边，烽火台的汉兵厉声盘问。吴军诈称是商船，要求靠岸避风，汉兵信以为真。约至二更，船上吴军突然袭击，占据了烽火台。随后，吕蒙带兵长驱直入，轻取荆州。吕蒙作战勇猛，平时却不肯读书。孙权劝道：你读点历史和兵法，用兵更高明。孙权道：汉先武帝从前行伍出身，却‘手不释卷’。从此，吕蒙勤勉自学，受益匪浅。手不释卷：手里不离开书本，形容读书勤奋。', ''],
            '首鼠两端': ['这句成语见于《史记·魏其武安侯列传》：“武安已罢朝，出止车门，召韩御史大夫载，怒曰：‘与长孺共一老秃翁，何为首西汉武帝时，王太后有个同母异父的弟弟叫田蚡。他靠着王太后的势力做了丞相，掌握大权。田蚡是个卑鄙阴险、骄横自私的人物，因为有王太后这座靠山，加之汉武帝当时还年轻，所以他胡作非为，骄横奢侈，营私舞弊，随意诬陷自己所不快的人。田蚡向窦婴要城南田，窦婴不给，又听说灌夫也替窦婴抱不平，由此跟灌夫和窦婴结了怨（窦婴和灌夫都是在平定七国之乱中立了功的大臣）。又因为灌夫掌握着田蚡贪污受贿的事，所以田蚡欲将他和窦婴置之死地有一次，田蚡结婚，王太后为了扩大自己的势力，便下了诏书，吩咐诸侯、宗室、大臣们都到丞相府去祝贺。窦婴和灌夫也去了。酒席上，灌夫因向客人敬酒遭到冷遇，气得破口大骂起来。为此，田蚡拘捕了灌夫。此事闹到了武帝那里，武帝便召集大臣们来研究。窦婴坚决反对对灌夫治罪，有的大臣则赞成治罪，有的惧伯田蚡的威势，采取模棱两可的态度。御史大夫韩安国说：“灌夫在平定七国之乱时，立了大功，虽说酒后闹事，但没有死罪。可丞相说他不对，也有道理，究竟如何处置，请皇上定吧！”洞外时，总是左顾右盼，畏首畏尾，故称“首鼠两端”，人们常用这句成语形容迟疑不定或动摇不定。 ', ''],
            '熟能生巧': ['宋代有个叫陈尧咨的人，射箭技术极为高超，常因此而骄傲。一天，他正在给大家表演射箭，箭全射中靶心，于是就向旁边卖油的老头吹嘘起来。然而老人却说：没有什么了不起，只不过是手法熟练而已罢了。说着，拿来一个葫芦，在葫芦口放上一枚铜钱，用勺子舀了一勺油，高高地举起倒了下去。倒下去的油像一条线一样穿过钱眼而过，金部流进了葫芦，而铜钱上一点油也没沾上。老头说：干任何事都一样，熟能生巧。这个成语指做事熟练了，就会掌握窍门，做得更好。 ', ''],
            '双管齐下': ['唐朝人张瑽，官为员外郎。不久，他从员外郎的地位降为衡州司马。后来，他又被调为忠州司马，在官场上很不得志。但是，他喜欢绘画。而且画得很好。他尤其擅长画松石山水。他画松树时，总是双手各握一支毛笔。他用一支笔画新枝，另一支笔画枯枝。用两支笔画出来的松树，不论是新枝还是枯枝，都生动逼真。人们喜欢他的画，纷纷上门求索。大家称赞他的画为神品。他绘画的方式，则被人们称为双管齐下。成语双管齐下原指手握双管同时作画。后用来比喻为了达到某一目的，同时采用两种办法或两件事同时进行。 ', ''],
            '水滴石穿': ['宋朝时，张乖崖在崇阳当县令。当时，常有军卒侮辱将帅、小吏侵犯长官的事。张乘崖认为这是一种反常的事，下决心要整治这种现象。一天，他在衙门周围巡行。突然，他看见一个小吏从府库中慌慌张张地走出来。张乘崖喝住小吏，发现他头巾下藏着一文钱。那个小吏支吾了半天，才承认是从府军中偷来的。张乘崖把那个小吏带回大堂，下令拷打。那小吏不服气：一文钱算得了什么！你也只能打我，不能杀我！张乘崖大怒，判道：一日一钱，千日千钱，绳锯木断，水滴石穿', ''],
            '水落石出': ['苏轼，字子瞻，号东坡居士，是名文学家苏洵的长子。神宗当皇帝的时候，采用王安石的变法政策，苏轼因不赞成新法，和王安石辩论。那时王安石很为神宗所器重，苏轼敌不过他，被贬到湖北当团练副使，他在黄州的东坡地方，建筑了一间居住，所以又称苏东坡。自号东坡居士。苏东坡喜欢山水，时时出去游玩。赤壁是三国时东吴和蜀汉联军大破曹操的地方；但赤壁在湖北有三处，一在汉水之侧，竟陵之东，即复州；一在齐安之步下，即黄州；一在江夏之西南一百里，今属汉阳县。江夏西南一百里之赤壁，正是曹公败处，东坡所游之赤壁在黄州汉川门外，不是曹公失败的地方，东坡自己也知道，他先后做了两篇赤壁赋，只是借题发挥而已，名同地异，因他的才思横溢，文笔流利，写得唯妙唯肖，使后人对于赤壁这地方，都怀有向往的心情，在后赤壁赋中，他有这样几句“...于是携酒与鱼，复游于赤壁之下，江流有声，断岸千尺，山高月小，水落石出，曾日月之几何，而江山不可复识矣。…”“水落石出”苏轼的赋中，本来是指冬的一种风景，但后人把这水落石出四字，用做真相毕露被悉破的意思。也有人把一件事情的原委弄清楚以后，等到真相大白，也叫做水落石出。 ', ''],
            '水深火热': ['齐国出兵攻打燕国。战场上一片混乱，老百姓家破人亡。齐宣王亲自督战，十分得意。齐国大小官员，有的赞扬齐宣王的壮举，有的私下里批评君主不仁不爱。孟子是大学问家，历来主张仁爱，反对战争，他当然很不高兴。齐宣王凯旋归来，设酒宴招待文武百官。齐宣王说：有人对我攻打燕国有意见，现在我50天就征服了他们，这不是天意吗？群臣们一声不吭，你看看我，我看看你。孟子，你倒说说看。齐宣王有点咄咄逼人。孟子回答说：如果您占领燕国，燕国人民很高兴，您就去占领吧！齐宣王很不高兴。孟子继续说：如水益深，如火益热，燕国的百姓会来送水、送饭，争相欢迎吗？成语水深火热本意是：使得水更加深，火更加热。比喻人民生活极端痛苦，如处在深水、热火之中。 ', ''],
            '司空见惯': ['唐代诗人刘禹锡，因为性格放荡不羁，在京中受人排挤，被贬做苏州刺史。当地有一个曾任过司空官职的人名叫李绅，因仰慕刘禹锡的诗名，邀请他饮酒，并请了几个歌女在席上作陪。席间，刘禹锡一时诗兴大发，作诗一首：高髻云鬓新样妆，春风一曲杜韦娘，司空见惯浑闲事，断尽苏州刺史肠。司空见惯这句成语，就是从刘禹锡这首诗中得来的。诗中所用的司空两个字，是唐代一种官职的名称，相当于清代的尚书。从刘禹锡的诗来看，整句成语的意思，就是指李司空对这样的事情已经见惯，不觉得奇怪了。这是一句很常用的成语，但有很多人仍会把它用错，因为寻常的事情，如果是发生得很自然，便不可以引用这句成语。如早晨的时候，太阳从东方出来，到黄昏的时候，太阳便在西方没落，这样便不能说司空见惯。有些事情发生得很偶然，但又是常常可能发生或见到的，这时用这个成语就比较恰当。比方大都市街道上的车辆，平常都是很安全地来往着，但很多时候又会发生意外，不是辗伤了人，便是撞了车，这样的事情我们看多了，则用司空见惯四个字就恰当了。 ', ''],
            '死不旋踵': ['“死不旋踵”原作“死不还踵”。这个成语，原出自《淮南子·泰族训》。原文说：“墨子服役者百八十人，皆可使赴火蹈刃，死不还踵。”意思是：春秋战国之际的著名思想家墨子的学生有180人，他们都是不避艰险、奋不顾身、至死也不会回头的人物。《后汉书·党锢列传·李膺传》里记载着“死不旋踵”的故事。东汉桓帝时代，宦官专权，与大官僚集团斗争十分激烈。世家豪族李膺做司隶校尉时，宦官头子张让的弟弟张朔做野王（现在河南省沁阳县）县令，贪赃枉法，凶暴残民，甚至杀戮孕妇。张朔害怕受到李膺的惩罚，于是畏罪逃到张让家里，躺在一根空心的屋柱内。李膺知道这个情况后，亲率役卒，冲进张让家里，砍破屋柱，把张朔捉来杀了。张让向桓帝告状，桓帝召李膺进宫，责问他为什么不先请示就把张朔处以死刑。李膺回答说：“现在我到任已经10天了，怕犯了积压案件的过失，想不到竟得了办案快的罪名。我自知有罪，死期就在眼前，但我并不惧怕（原文是“诚自知衅责，死不旋踵”），特请宽限5天，让我把那些坏蛋惩办完，卸了任再来受刑。”桓帝听了，回头对张让说：“这是你弟弟罪有应得，司隶校尉有什么过错？”“旋踵”是转动脚后跟，即后退的意思，有时也比喻时间很短。后来，人们引用“死不旋踵”这个成语，来比喻不避艰险，即使死也不后退或死在眼前也不怕。 ', ''],
            '死而不朽': ['公元前549年，鲁国的大夫穆叔奉命到晋国去访问。晋国的卿范宣子接待了他，并且与他交谈起来。范宣子问穆叔道：“古人有话说：‘死而不朽。’你知道它说的是什么吗?”穆叔不清楚范宣子提出这个问题的用意，没有马上口答。范宣子以为穆叔答不上，得意他说：“我的祖先，虞舜前是陶唐氏，夏朗后是御龙氏，在商朗是象韦氏，在周朝则是唐社氏。周王室衰败以后，由晋国主持中原的盟会，执政的是范氏。所谓‘死而不朽’，恐怕说的就是这个吧!”穆叔听他这样说，觉得很不入耳，便说：“据我所听到的，这叫做世禄，也就是世世代代享受禄位，而不是‘不朽，。鲁国有一位已经去世的大夫，叫藏文种。死了以后，他的话世世代代没有被人们废弃。所谓‘不朽’。，说的是这个吧。”他接他又说：“我听说，最高的是树立德行，其次是树立功业，再其次是树立言论。如果能做到这样，虽然死了也久久不会被人们废弃。这叫做三不朽。若只是保存和接受姓氏，用来守住宗庙，世世代代不断绝祭祀，那是每个国家都有的，不能说是不朽。', ''],
            '死灰复燃': ['西汉时，韩安国是汉景帝与梁孝王身边一个很受欢迎的人。但是他年轻的时候，也曾经发生过一段曲折的故事。由于受到某件事的牵连，他被送进监狱等最后的判决下来。在监狱里有一个叫田甲的看守，对他非常不礼貌，常常毫不留情地羞辱他。有一次安国被欺负得太过份，就告诉田甲说：“你不要以为我这辈子就没有出人头地的一天，暂时熄了火的灰烬，难道就没有可能再烧起来吗？”田甲得意地说：“如果会的话，我一定会撒泡尿浇熄它。”可是，过了不久，安国无罪释放，而且还当上了大官。这时，田甲只好低头向韩安国认错。', ''],
            '死里逃生': ['从前楚国有个人叫次非，在一次机会中得到一把宝剑，便高兴地渡河回家。当船划到河中心的时候。突然出现两条蛟龙，绕着他的船兴风作浪。船上的人都叮坏了，不知道该怎么样辨。次非却镇争地问船夫：“照这样下去的话，全船的人不是等死吗？”。船夫消极地说：“这注定必死无疑，还能有什么辨法呢？”次非沉思片刻，立刻拔出宝剑说：“以前丢了性命的人，之所以会死在这里，就是因为他们虽然有武器，但不敢和蛟龙拼命。”次非一说完话，便跳进江里，杀了这两条蛟龙。全船的人也就得救了。', ''],
            '随珠弹雀': ['《庄子·让王篇》有这么一个故事：鲁侯（或谓即鲁哀公）听说颜阖是个贤明的人，想请他出来为国家出点力，便派人先送一份礼物去。颜阖家里很穷，住在一个破烂的村子里，这一天正披着件粗麻布旧衣，在那儿喂牛。鲁侯派的人来了，向颜阖问道：“喂，这儿是颜阖的家吗？”颜阖说：“是的，这是我的家。”那人这才知道他就是颜阖，便说明来意，把带去的礼物当面交给他。颜阖不受，说：“恐怕你听错了？要是送错，你会获罪的，还是回去问问清楚吧！”那人就这样被打发走了。可是不一会，又来了，说：“没有错，就是送给您的，无论如何，求您一定收下！”那人放下礼物就走，颜阖还有什么办法推辞呢。仞之雀，世必笑之。是何也？则其所用者重而所要者轻也！”比喻所用代价太大而收获太微、得不偿失，后来就叫“随珠弹雀。”（“随”也可以写作“隋”。春秋时随国在今湖北随县，为楚国所灭。南北朝时，杨坚受封于随，他把“随”改名为“隋”。后来杨坚做了皇帝，又以“隋”为国号，即隋朝，他就是隋文帝。从此，“随侯之珠”，也写作“隋侯之珠”。）', ''],
            '所向无前': ['岑彭字君然，南阳棘阳（今河南新野东北）人。王莽末年，岑彭为南阳棘阳县令，因为汉兵攻破城池，他逃奔到前队大夫甄阜那儿。甄阜令岑彭戴罪立功，坚守城池。后因汉兵攻打数月，城中粮尽，岑彭不得已开城投降。汉将想杀岑彭，大司徒伯升劝解说：岑彭是一郡之长官，坚心为其主守城，那是忠节。现在他归附我们，是相信正义，应当鼓励。这样，更始帝便封岑彭为归德侯。后来，他们又归顺了刘秀。待刘秀即位（为光武帝）后，岑做了廷尉，行使大将军的职权。从建武元年至11年，岑彭多次率部队南征北战，为东汉王朝屡立战功。', ''],
            '泰山压卵': ['孙惠是晋惠帝时齐王冏的谋士。在齐王失败之后，孙惠受到了成都王的重用，后来成都王起兵攻打长沙王，孙惠十分失望，才退隐。不久，东海王在下邳起兵，孙惠知道，就上书东海王，指出历代王朝危亡的情形，都是枝叶先雕零，才引起上下根株的死亡。因此，劝东海王应该一心平乱，匡扶王朝。同时还颂扬东海王的实力：“这种强大的力量，就像是乌获摧毁冰块；令孟贲折断枯树；使猛兽吞食狐狸；用泰山来压卵一样，这是没有办法相比的……”最后，东海王被孙惠恳切的言词打动，才起用了他。', ''],
            '贪得无厌': ['智伯，是春秋时代的人，他的野心很大，有一次他还联合了韩、赵、魏三国，把中行氏给灭掉，侵占了中行氏的领土。过了几年，他又派人向韩国要求割地，韩国惧怕，就给了他一块有万户人家的土地。智伯这回知道了食髓知味，又向魏国要求割地，魏国本来不想给，但是也怕围攻，只好和韩国一样，也给了他一块土地。智伯心中更高兴了，向赵国索取蔡和皋狼这两个地方；但是赵襄王拒绝了，智伯便结合韩国和魏国要攻打赵国。赵襄王采用谋士的计策，迁都晋阳，准备了充足的粮食来抵抗智伯。这样经过了三年，智伯始终没有办法攻下晋阳。但是，赵国的粮食快要用完了，派人去游说魏和韩，教他们联合起来，倒戈攻打智伯。因为智伯的野心太大了，魏国、韩国就答应了。于是，赵国连夜出兵，韩、魏两国跟着响应，把智伯击败，并瓜分他的土地；当时，天下的人不但不同情智伯，反而讥笑他“贪得无厌”，得到报应。', ''],
            '贪小失大': ['战国时，秦国想并吞近邻的蜀国，但由于秦蜀之间的秦岭山高路险，攻取不便。有人给秦王出了条妙计，秦王听后非常高兴，立刻派人用石头凿刻了一条石牛，在后面放了许多金银财宝，说是石牛拉出来的粪便。然后把石牛放在秦蜀之间的路上，作为礼物送给蜀王。蜀王听说后，马上令人开山修路。路修好后，秦兵以护送石牛为由，开始进攻蜀国，蜀国因此而灭亡。这个成语比喻因贪图小利而造成重大损失', ''],
            '坦腹东床': ['晋代太傅郗鉴，派一位门客到丞相王导家里去选女婿。王导告诉门客说：“你到东面的房子里，任意挑选吧︰”门客回来告诉郗鉴说：“王家的男孩都很好，听说我来选女婿，就都拘谨起来。只有一个男孩在东面的床上露着肚子躺着，好象没听见似的。”郗鉴说：“这个人做女婿最好。”原来，这个人就是王羲之，于是郗鉴把女儿嫁给了他。', ''],
            '探骊得珠': ['很久很久以前，有一户人家住在黄河边上，靠割芦苇、编帘子簸箕为生，日子过得非常贫困。', ''],
            '螳臂当车': ['颜阖担任卫灵公大儿子蒯瞆的老师，但蒯瞆自以为将来会当国君，作威作福，蛮不讲理。颜阖感到十分为难，于是对卫国大夫蘧伯玉诉苦。蘧伯玉劝他说：“你的意图是好的，但实际上是不可能的。你知道嘛，螳螂吗想举起它的臂膀，以挡住前进中的车子，这是不可能的啊！” ', ''],
            '天夺之魄': ['公元前５９４年，狄人（赤狄）丞相丰舒执政后杀了他的国君潞子婴儿的夫人，又伤了潞子的眼睛。潞子的夫人是晋景公的姐姐。因此，晋国在同年夏季出兵攻打赤狄，不到一个月的时间，即灭了赤狄。君的先人）去向周朝的天子进献俘虏的狄人。赵同依仗晋国强大，对周天子表现得很不恭敬，很傲慢。周天子的儿子刘康公看了很不高兴，骂道：“不及１０年，原叔（即赵同）必有大咎，天夺之魄矣！”意思是说，要不了１０年，赵同必定遭到大祸，老天爷已将他的魂魄夺走了。“天夺之魄”这个成语用来比喻人已离死期不远了。', ''],
            '天花乱坠': ['两晋南北朝时佛教盛行，全国有寺庙3万多所，僧尼200多万。南朝的梁武帝带头求神拜佛，在全国大建寺庙。他曾经三次舍身同泰寺，他还聘请古印度僧人波罗末到中国讲经。波罗末翻译了不少印度佛经，并培养了许多中国弟子。有了经书，讲经的风气更加兴盛。为了宣传民众，佛教徒编了许许多多讲经的传说。其中一则是：云光法师讲经，感动了上天，天上的鲜花纷纷坠落。后来，佛教在中国分成许多宗派，影响最大的是“禅宗”。宋真宗时，道原和尚编了一本《景德传灯录》，记载了禅宗师徒的故事。书中讲到对佛意要真正领会，反对“讲得天花乱坠”。从此，人们用“天花乱坠”来形容说话极其动听，但多指过分夸张，不切实际。', ''],
            '天经地义': ['公元前520年周景王姬贵死后，按习俗由他正夫人所生的世子姬敬继位。但是，景王生前曾与大夫宾孟商讨过，打算立非正夫人所生的长子姬朝为世子。这样，姬朝也有资格继位。于是，周王室发生了激烈的王位之争。', ''],
            '天罗地网': ['元朝李寿卿写了一本《伍员吹箫》的杂剧，内容是这样的：春秋时代，楚平王听信奸臣费无极的怂恿，把太子的妻子改作自己的妻子。太子的老师是太傅伍奢，是个刚正不阿的人。费无极怕伍奢帮助太子惩罚他，又怂恿楚平王杀害了伍奢及其全家人。太子得到消息，连夜逃走了。太子知道伍奢的第二个儿子伍员镇守樊城，就日夜兼程，赶到樊城。他把伍奢全家被害的情况告诉了伍员，并叫他提防。费无极果然派儿子费得雄来见伍员，说楚平王因伍员有功，召他返朝受赏。伍员怒斥道：若不是太子报信，我险些被打入天罗地网。伍员把费得雄痛打一顿，弃官逃到吴国，在街上吹箫求乞。后来，伍员受到吴王的重用，终于发兵伐楚，报了杀亲之仇。天罗地网，就是天为罗，地为网，比喻四周包围得十分严密，难以逃脱', ''],
            '天下无双': ['信陵君魏无忌窃符救赵后，怕哥哥魏王追究，避居赵国。他听说毛公和薛公很有才能，便去邀请。但两人不肯来见。他打听到毛公藏在赌徒中，薛公藏在卖酒人家，便去寻访，终于结识了两人。', ''],
            '天涯海角': ['韩愈，字退之，是唐代中叶时的伟大文学家。他二岁时就死了父亲，不久他的母亲又死去。幼时依靠他哥哥韩会和嫂嫂郑夫人过活。韩会有一个嗣子（愈次兄介之子，出继与长兄会为嗣）叫老成，排行十二，所以小名叫十二郎，年纪比韩愈小一点。后来韩会四十二岁的时候，因宰相元载的事，贬为韶州刺史，不到几个月就病死在韶州，这时韩愈只有十一岁，十二郎也很小。韩愈虽然有三个哥哥（会、弁、介），都很早离开了人世。这时，继承祖先后代的，只有韩愈和他的侄子十二郎两个人，零丁孤苦，没有一天离开过。', ''],
            '天衣无缝': ['古时候有个叫郭翰的先生，他能诗善画，性格诙谐，喜欢开玩笑。盛夏的一个夜晚，他在树下乘凉，但见长天如碧，白云舒卷，明月高挂，清风徐来，满院飘香。这时，一位长得异常美丽的仙女含笑站在郭翰面前。看，很诧异仙女的衣服是没有缝的。 ####仙女说：天衣无缝，你连这个都不懂，还称什么才子，我看你是十足的大傻瓜。 ####郭翰听完哈哈大笑，再一瞧，仙女不见了。', ''],
            '天真烂漫': ['南宋末年，有位姓郑的画家曾以太学生的资格，参加博学词科考试。后来北方蒙古贵族南侵，他向朝廷上书主张抵抗，但未被采纳', ''],
            '天之骄子': ['西汉时，匈奴常侵扰边郡。汉武帝派兵出击，多次得胜。公元90年，匈奴骑兵又侵占五原、酒泉，杀掠当地百姓。汉武帝派大将李广利等率军反击匈奴。匈奴单于（最高首领）丢弃了粮草、武器，却保存着实力。李广利大败匈奴。这时，他家属犯罪下狱的消息传来，他很担忧。谋士献计要他将功折罪。于是他挥兵北进，浴血沙场。后匈奴单于又乘机领兵袭击李广利。他招架不住，便投降了。单于为了笼络住李广利，把女儿嫁给他。一年后，李广利遭到匈奴丁灵王卫律的嫉妒，被害死。单于致书汉武帝：强胡，天之骄子。他要汉朝每年赠他美酒、绸缎等。汉武帝只得承认强胡难灭，以后与匈奴时和时战。匈奴人自称天之骄子即为天所骄宠，故极强盛。后也指非常勇敢或有特殊贡献的人。 ', ''],
            '同仇敌忾': ['东周春秋时期，有一首流传于军中的歌谣，表现了士兵们慷慨从军；同心对敌的乐观精神和保卫祖国的英雄气概。这首歌谣分为三节，可以反复咏唱。其中第一节是这样的：”谁说没有衣服?我的战袍就是你的。国王兴兵打仗，快把刀枪修好。我与你共同对付仇敌。”“同仇”这个词就来源于上面的歌谣。公元前623年，卫国的宁俞出使鲁国，鲁文王设宴招待。席间，文王让乐工演唱《湛露》和《彤TONG弓》，宁俞一听就知道。这是周天子对诸侯恩赐、褒奖时的宴乐。为此，他在席间不作任何答谢之辞。文王对宁俞在席间表示沉默不理解。宴饮完毕后，命人私下询问他是什么原因。宁俞回答说：“当年诸侯以周天子对敌人的愤恨为同恨，所以为天子献上战功。天子为了酬谢诸侯，在酒宴中赐彤弓，赋《湛露》，这是应该的。但如今我们卫国来到鲁国表示友好，大王学天子赐诸侯的礼节，也命乐工演唱《湛露》和《彤弓》。在这种情况下，我只好沉默不言了。”“敌忾”这个词就来源宁俞说的话。 ', ''],
            '同甘共苦': ['战国时，燕国太子姬平继承了王位，史称燕昭王。怎么治理，才能富民强国，燕昭王真感到束手无策。一天，他听说郭隗善出点子，很有计谋。于是赶紧派人去把郭魄请来，对他说：“你能否替我找到一个有本领的人，帮我强国复仇?”郭魄说：“只要你广泛选拔有本领的人，并且要亲自去访问他，那么，天下有本领的人就都会投奔到燕国来。”“那么我去访问哪一个才好呢?”郭隗回答说：“先重用我这个本领平平的人吧!天下本领高强的人看到我这样的人都被您重用，那么，他们肯定会不顾路途遥远，前来投奔您的。”燕昭王立刻尊郭隗为老师，并替他造了一幢华丽住宅。消息一传开，乐毅、邹衍、剧辛等有才能的人，纷纷从魏、齐、赵等国来到燕国，为燕昭王效力。燕昭王很高兴，都委以重任，开关备至；无论谁家有婚丧娶等事，他都亲自过问。就这样，他与百姓同事安乐，共度苦难二十八年，终于把燕国治理得国富民强，受到举国上下的一致拥戴。 ', ''],
            '同工异曲': ['唐代杰出的散文家韩愈。曾经担任过国子监博士。他学识渊博，讲起课来旁征博引，兼通百家，出口成章，妙语连珠，深受大学生们的欢迎。有一次，他写了一篇题为《进学解》的文章，来发泄自己才学极高却遭到贬斥的愤感情绪。一天早上，韩愈教导大学生们说：“学业由勤奋而精进，由嬉游而荒废；为人行事由深思远虑而获得成就，由因循、随便而道致毁败。如今圣上和群臣融洽相处，公正无私，有才能的人都得到了任用，谁说才多反而不被举用?”说到这里，大学生们哄堂大笑起来，有人站出来问道：“先生在骗人!弟子跟先生学了几年，深知先生终年苦学不倦，对待学业可称得上是非常勤奋。先生埋头于儒家典籍之中，玩味它的精华，然后写成文章，住处内充满了自己的著作。上取法学习于虞舜、夏禹时代的著述，《尚书》、《诗经》，下及《庄子》、《史记》以及西汉扬雄和司马相如的著作，它们各有特色，都是好文章，就像乐曲虽不同，都同样美妙动听。先生的文章内容丰富，语句洒脱畅达。先生的为人行事，也早巳由深思远虑而获得成就，但为什么自己常常弄得进退两难呢?”', ''],
            '投笔从戎': ['班超是东汉一个很有名气的将军，他从小就很用功，对未来也充满了理想。有一天，他正在抄写文件的时候，写着写着，突然觉得很闷，忍不住站起来，丢下笔说：“大丈夫应该像傅介子、张骞那样，在战场上立下功劳，怎么可以在这种抄抄写写的小事中浪费生命呢！”', ''],
            '投鼠忌器': ['三国初期，汉献帝与丞相曹操、皇叔刘备一起去打猎。曹操为了显示自己的武力，竟跟汉献帝齐头并进。汉南帝见不远处有只兔子，就叫刘备射，说是要看看皇叔的箭法。刘备连忙弯弓射箭，正好命中兔子，献帝连夸好箭法。南帝又看见一只大鹿，连射三箭不中，就叫曹操射。曹操拿过南帝的金比箭，一箭就射中了鹿。将士们见射中鹿的是金比箭，以为是献帝射的，都高呼万岁，曹操得意地站到献帝前接受欢呼。关云长实在看不下去，要拍马刀砍曹操，刘备忙暗示他不可轻举妄动。事后，关云长问刘备为什么不让杀曹操，他说：投鼠忌器，他身边还有献帝呢。投鼠忌器的意思是老鼠靠近器物，用东西砸老鼠又怕砸坏老鼠附近的用具。现常用来比喻做事有所顾忌，不敢放手进行。', ''],
            '图穷匕见': ['战国时，荆轲奉燕国太子丹的命令，以燕国的地图作为礼物献给秦王，匕首就藏在地图卷里，试图伺机刺杀秦王，但最后失败。《战国策？燕策三》：“轲既取图奉之，发图，图穷而匕首见。”', ''],
            '屠龙之技': ['有个人叫朱泙漫，他想学一种出奇的本领，听说支离本领”。', ''],
            '土崩瓦解': ['商纣王是商朝的末代君主，是一个暴虐无道的昏君。他贪恋酒色、荒淫无度，整日花天酒地，寻欢作乐，不理朝政。队从容关一直驻扎到蒲水。士兵不下数万，但打起仗来，因为兵士不愿意为纣王战死，所以“倒矢而射”把兵器扔在一边。商朝军队士气如此低落，商朝的政权自然是岌岌可危了。', ''],
            '兔死狗烹': ['越王句践大夫范蠡，曾经替越国出过了不少力，使得越国得以打败吴国，成为霸王。对越国来说，范蠡可是个大功臣，本来他是可以安享富贵的，但是范蠡却没有这么做，他宁愿舍弃荣华富贵，而自行引退，过着淡泊的生活。就在众人一片惋惜声中，范蠡又托人带了一封信给从前的同事大夫文种，他劝文种也舍弃功名富贵，以免招惹灾祸。范蠡为什么会这样劝文种呢？原来，他早就看出越王是个只能共患难，却不能共享乐的人，所以他在信中说道：“……飞鸟尽，良弓藏，狡兔死，走狗烹，……”，“兔死狗烹”就是从信中这几句话引申出来的。国，终于被杀，这就是“兔死狗烹”，也就是一般人所说的“有事就用你，无事就给你一个罪名”这句话。 ', ''],
            '退避三舍': ['春秋时候，晋献公听信谗言，杀了太子申生，又派人捉拿申生的弟弟重耳。重耳闻讯，逃出了晋国，在外流忘十几年。', ''],
            '脱颖而出': ['战国时，秦国攻打赵国。赵国平原君奉命到楚国求助，毛遂请求跟着去。平原君说：“有本事的人，在人群中，就如锥子放在布袋中，尖儿立刻露出来。你在我家已有三年，但我未听说过你的名字。看来你没有什么能耐，还是不要去了。”毛遂说：“若我真的能如锥子，放在布袋里，就会连锥子上面的环也露出，岂止只露出尖儿︰”后来毛遂就跟着去，并起了非常重要的作用。', ''],
            '外强中干': ['春秋时代的晋献公死后，晋公子夷吾结束逃亡生活，回到晋国继承王位当上了国君。很快就打到晋国的一个城镇，为了抵抗强大的秦军，晋惠公亲自领兵反抗。他下令拉战车的马，一定要用郑国的骏马。有位大臣看到，连忙对晋惠公说：郑国的马看起来虽然很强壮，但是实际上却很虚弱，打起仗来一紧张就会不听指挥。到那时，进退不得，大王还是不要做此决定吧！但是晋惠公一点都不愿意听大臣的劝告，果然，没多久晋惠公的马车就出不听指挥，而晋惠公一下就被秦军捉住，当了俘虏，晋国因此而大败。', ''],
            '完璧归赵': ['战国时代，赵王无意间得到了一块宝玉和氏璧，秦昭襄王听说后非常想要据为己有，因此就派人到赵国，对赵王说秦国愿意以十五个城与赵国交换这块玉。赵王心里非常舍不得，但是因为赵国国势很弱，因此不敢得罪秦王，怕秦王一不高兴，就派兵攻打赵国。为了这件事，赵王伤透了脑筋。', ''],
            '爱鹤失众': ['公元前668年，卫惠公的儿子姬赤成为卫懿公后，不思富国强兵之道，整天喜欢养鹤，甚至荒唐到给鹤封官位，享官禄，百姓怨声载道。北方狄国借机出兵攻打卫国，卫国士兵根本不抵抗就逃散，卫懿公被狄兵所杀。 ', ''],
            '爱屋及乌': ['因为爱一个人而连带爱他屋上的乌鸦。比喻爱一个人而连带地关心到与他有关的人或物。', ''],
            '安步当车': ['另外，“晚食当肉”也是一句成语，它和“安步当车”一样都是节俭的意思。 ', ''],
            '安居乐业': ['老子是这样描绘他所设想的小国寡民社会的：国家很小，人民稀少。即便有许许多多的器具，也不去使用它们。不要让人民用生命去冒险，也不向远处迁移，即使有车辆和船只，也无人去乘坐它们；即使有兵器装备，也无处去使用它们。要使人民重新使用古代结绳记事的方法，吃得很香甜，穿得很舒服，住得很安适，满足于原有的风俗习惯。邻近各国互相望得见，鸡鸣狗叫互相听得见，但是人们直到老死，也不互相往来。 ', ''],
            '安然无恙': ['公元前266年，赵国国君赵惠文王去世，他的儿子太子丹接位为赵孝成王。由于孝成王还年轻，国家大事由他的母亲赵威后负责处理。赵威后是一个比较贤明而有见识的中年妇女。她刚刚主持国事的时候，秦国加剧了对赵国的进攻。赵国危急，向齐国求救，齐国要赵威后把她的小儿子长安君送到齐国作人质，然后再出兵。赵威后舍不得小儿子离开，但是听了大臣触龙的意见，还是把长安君送到齐国。齐国出兵帮助赵国打退了秦军。', ''],
            '安如泰山': ['关国是当时诸侯中的大国，吴王刘濞野心很大，对中央政权心怀怨望，暗中图谋叛乱。汉景帝任用富有才能的政治家晁错为御史大夫，晁错主张削减各诸侯国的领地，加强中央的权力和威信，巩固国家的统一。刘濞看到一些诸侯王纷纷被削减了领地，知道自己也在所难免，于是联络楚、赵、胶西、胶东等国的诸侯王阴谋策划叛乱。', ''],
            '按兵不动': ['春秋末，晋国东部的卫国是个弱小的诸侯国。被迫与晋国结盟，实际上完全听命于晋国，不住地给晋国进贡财物。当时任国君的卫灵公不愿长久处于屈辱的地位，便与齐景公缔结盟约，从而与晋国断绝了关系。', ''],
            '按图索骥': ['春秋时，秦国的伯乐很善于鉴别马匹。他把自己识马的知识和经验写成一本书，叫《相马经》。书中图文并茂地介绍了各类马匹。', ''],
            '暗渡陈仓': ['楚汉相争时，项羽凭借强大的实力，违背先入关中者为王的约定，自立为西楚霸王，把汉中和巴蜀一带封给先入关中的刘邦。刘邦听从谋士张良的计策，到汉中时，人马过后，烧毁沿途的栈道，表明自己不再回关中了。项羽从此放松了对刘邦的警惕。后来，刘邦拜韩信为大将，命士兵修复原来烧毁的栈道，装作要从栈道出击进攻关中的样子，实际上却带领主力部队抄小道趁守将不备袭击了陈仓，进而攻人咸阳，占领了关中，揭开了楚汉大战的序幕。 ', ''],
            '暗箭伤人': ['春秋时，郑国联合鲁、齐两国共同讨伐许国。在攻打许国都城时，老将颖考叔手执大旗，登上城头。青年副将公孙子都眼看颖考叔就要立大功，心怀忌妒，对他暗放一箭，正中背心。颖考叔顿时一个跟头栽下城来。另一副将瑕叔盈还以为他是被敌人射死的，马上拾起大旗，继续指挥战斗。最后，郑军终于攻克了许国都城。人们称公孙子都向颖考叔放暗箭是暗箭伤人。暗箭伤人：比喻用阴险的手段暗中攻击或陷害别人。 ', ''],
            '八面威风': ['这个成语来源于元.郑德辉《三战吕布》，托赖着真天子百灵威助，大将军八面威风。元朝末年，封建朝廷愈加腐败，各地农民纷纷举起义旗，反抗元朝的统治。这时朱元璋已经领兵攻下安徽,和阳，准备继续南下。在过年那天，他与大将徐达，同乘一条小船，从长江北岸渡过长江。船主是对老夫妻，船夫知道船上坐着的是大名鼎鼎的朱元璋，便高声喊看号子向他庆贺说：圣天子六龙护驾，大将军八面威风。朱元璋明白这是祝贺帝王的话，心里非常高兴，便和徐达轻轻地踢着脚，互相表达庆贺之意。后来朱元璋统一全国，建立了明朝，他成为历史上闻名的皇帝明太祖。明太祖找到当年的船夫，给了他封赏，又将他那只小船涂上朱红颜色，表示有功。" ', ''],
            '八仙过海': ['传说吕洞宾等八位神仙去赴西王母的的蟠桃会，途经东海，只见巨浪汹涌。吕洞宾提议各自投一样东西到海里，然后各显神通过海。于是铁拐李把拐杖投到水里，自己立在水面过海；韩湘子以花蓝技水而渡；吕洞宾、蓝采和、张果老、汉钟离、曹国舅。何仙姑也分别把自己的萧、拍板、纸驴、鼓、玉版、竹罩投到海里，站在上面逐浪而过。八位神仙都靠自己的神通渡过了东海。八仙过海根据这个传说而来。八仙过海比喻各自有一套办法或本领去完成任务。 ', ''],
            '拔苗助长': ['这个成语来源于《孟子.公孙丑上》，宋人有闵其苗之不长而揠之者，芒芒然归，谓其人曰：今日病矣！予助苗长矣！其子趋而往视之，苗则槁矣。《孟子》是一部儒家经典，记载了战国时期著名思想家孟轲的政治活动、政治学说和哲学伦理教育思想。这部书中有个故事十分有名：宋国有一个农夫，他担心自己田里的禾苗长不高，就天天到田边去看。可是，一天、两天、三天，禾苗好象一点儿也没有往上长。他在田边焦急地转来转去，自言自语地说：我得想办法帮助它们生长。一天，他终于想出了办法，急忙奔到田里，把禾苗一棵棵地拔，从早上一直忙到太阳落山，弄得精疲力尽。他回到家里，十分疲劳，气喘吁吁地说：今天可把我累坏了，力气总算没白费，我帮禾苗都长高了一大截。他的儿子听了，急忙跑到田里一看，禾苗全都枯死了。孟轲借用这个故事向他的学生们说明违反事物发展的客观规律而主观地急躁冒进，就会把事情弄糟。 ', ''],
            '拔山举鼎': ['这个成语来源于《史记.项羽本纪》，籍项羽长八尺余，力能扛鼎，才气过人。又：力拔山兮气盖世，时不利兮骓不逝。项羽，名籍，秦末下相人。少年时代，项羽不喜欢读书写字，改学击剑，也不肯好好学。叔父项梁很生气，项羽说：“学写字只要能记记姓名就够了。击剑是对付个把人的，也不值得学，我要学习抵敌万人的本领。”项梁于是教他兵法，他很高兴，但也只求略知大意，不肯认真钻研。据说，项羽二十二三岁时，身体魁梧，体力强壮，能把几百斤重的鼎举起来。后来，项羽起兵反秦，接着又同刘邦争夺天下，从24岁开始，奋战了8年，最后被刘邦等包围在垓下，终于自刎于乌江。自刎前，在四面楚歌的那天晚上，项羽在营帐中对着爱妾虞姬和叫骓的名马，慷慨高唱道：力拔山兮气盖世，时不利兮骓不逝！骓不逝兮可奈何？虞兮虞兮奈若何！ ', ''],
            '拔帜易帜': ['韩信被刘邦拜为大将后，率领汉军攻占了魏国和代国，接着又在张耳的协助下，带了几万兵东下井陉，攻击赵国。赵王和主将陈馀在井陉口聚集了二十万大军阻挡。谋士李左军建议陈馀拔给他三万军队，从小路出发，出奇不意地截取汉军的后勤装备及粮食；而它的前军抵达井陉时不与交战。这样的话，不到十天就可以取下韩信和张耳的头颅。陈馀是个读书人，不爱使用诈谋奇计，认为韩信的兵不过数千，经过千里行军，巳非常疲惫，可以直接予以攻击，因此没有采纳李左军的计谋。韩信手下的人探听到这个消息后，十分高兴，放心东下井陉，进军到离井陉口三十里之处，韩信下令休息。半夜里，他选出两千名轻骑兵，让他们每人拿着一面红色旗帜，从小道来到井陉口山后隐蔽起来，同时对他们说：“我将另派一支军队与赵军对垒，并假装败退。这样，赵军必定倾巢而出，前来追击。你们乘此机会快速进入赵营，拔掉赵军的旗帜，换上我们汉军红色的旗帜。”接着，韩信又派出一支一万人的军队，叫他们背水摆开阵势。赵军见汉军排出兵法上最讳忌的背水之阵，都哈哈大笑，以为汉军自己断了后路。天刚亮，韩信指挥这一万人的军队向井陉口进发，赵军立即打开营门迎击。战了一段时间后，韩信、张耳命汉兵丢掉旗鼓，向水边退去。汉兵退到水边阵地，再也无法后退，只得拼死作战。这时，隐蔽在山后的两千汉兵，趁赵营无人守卫，快速冲进赵营，飞快地拔掉赵军旗帜，换上汉军红色的旗帜。而在水边作战的赵兵，因遇到背水一战的汉兵的顽强抵抗，无法取胜，想返回营地，却见那里全是汉军的红旗，以为赵王已被汉兵抓住，顿时军心大乱，各自逃命。接着，汉军两面夹击赵军，结果主将陈馀被杀，赵王被活捉。 ', ''],
            '白面书生': ['南北朝的时候，有一个人叫做沈庆之。沈庆之从小就非常会打仗，常常打胜仗回来，后来他被封为“建武将军”，专门负责防守边疆。有一天，皇帝想要向北边扩展领土，沈庆之知道了，就极力阻止皇帝：“大王，这件事万万不可，您还记得以前几位将军向北边扩展领土失败的事吧！大王...”沈庆之不停地劝皇帝，皇帝觉得很烦，就对沈庆之说：“我不想听了，我叫别人来跟你说！”皇帝就找了左右两个文官来和沈庆之争辩，沈庆之无奈地对皇帝说：“大王，治理国家就像治理家一样，要讨论耕田的事就要找每天去耕田的工人，要问织布的事就要找织布的婢女。现在大王要去攻打其它的国家，却去找两个从来没打过仗的〝白面书生〞来商量，这场仗怎么会成功呢？”皇帝不耐烦地说：“你不要再说了，我决定的事是不会再改变了！”皇帝没有采纳沈庆之的意见，最后当然打了个大败仗回来！后来，大家就用沈庆之说的“白面书生”用来形容年轻没有经验的读书人，只知道书本上的知识，不晓得实际应付事情的方法。', ''],
            '白头如新': ['西汉时期，邹阳有一次因为受人诬陷，被梁孝王关进监牢，准备处死。邹阳十分激愤，他在狱中给梁孝王写了一封信，信中列举事实说明：“待人真诚就不会被人怀疑，纯粹是一句空话。”他写道：“荆轲冒死为燕太子丹去行刺秦始皇，可是太子丹还一度怀疑他胆小畏惧，不敢立即出发。卞和将宝玉献给楚王，可是楚王硬说他犯了欺君之罪，下令砍掉他的脚。李斯尽力辅助秦始皇执政，使秦国富强，结果被秦二世处死。所以谚语说：‘有白头如新，倾盖如故。’双方互不了解，即使交往一辈子，头发都白了，也还是像刚认识时一样；真正相互了解，即使是初交，也会像老朋友一样。”梁孝王读了邹阳的信后，很受感动，立即把他释放，并做为贵宾接待。', ''],
            '白云亲舍': ['当时他的父母远在河阳（今河南孟县），一次，狄仁杰外出办事登上太行山，由于思乡情切，不由向河阳方向远眺，只见一片白云在天上孤零零地飘浮。狄仁杰指着那片白云对随行的人员说：“吾亲舍其下。”意思是，他的双亲就往在那片白云下面。他怅望了好仁杰是唐朝并州（今山西太原）人，他年轻时曾做过并州法曹参军。久，直到那片白云散云才离开。公元７００年９月，锹仁杰病逝，终年七十一岁。武则天闻讯，非常悲痛，流着眼泪说：“朝堂空矣！”传说，狄仁杰死后葬于邯郸磁县狄仁村，墓冢尚在。“白云亲舍”，比喻客居他乡，思念父母。 ', ''],
            '百步穿杨': ['《战国策·西周策》：楚国有个叫养由基的人，他的箭术非常高明，即使离开柳树一百步射它的叶子，也百发百中，在旁的人看见了皆齐声喝采。 ', ''],
            '百尺竿头': ['宋朝时，长沙有位高僧名叫景岑，号招贤大师。这位太师佛学造诣高深，时常到各地去传道讲经。一天，招贤大师应邀到一座佛寺的法堂上讲经。前来听讲的僧人很多，大师讲得深入浅出，娓娓动听，听的人深受感染。法堂内除了大师的声音外，一片寂静。招贤大师讲经完毕后，一名僧人站立起来，问他行了一个礼，然后提了几个问题，请求大师解答。大师还了礼，慢慢地作答起来。那僧人听到不懂处，又向大师提问，于是两人一问一答，气氛亲切自然。听讲的人发现，他俩谈论的是有关佛教的最高境界----十方世界的内容。为了说明十方世界究竟是怎么回事，招贤大师当场出示了一份偈帖。所谓偈帖，就是佛教中记载唱词的本子。但见大师指着上面的一段文字念唱道：百丈的竹竿并不算高，尚需更进一步，十方世界才算是真正的高峰。', ''],
            '百川归海': ['西汉的思想家、文学家刘安，是汉高祖刘邦的孙子，袭父封为淮南王。他爱好读书鼓琴，才思敏捷，曾召集宾客和懂得天文、医学、历算、占卜等数千人，集体编写了一部数十万字的书《鸿烈》，也称《淮南子》。《淮南子》中有一篇《汜论训》，讲了人类社会发展的一些情况，它的基本观点是符合历史唯物主义的。文章中写道：“我们的祖先早先住在山洞里和水旁边，衣着非常简陋，生活十分艰苦。后来出了圣人，他们带领人们建造宫室，这样人们才从山洞里走出来，住进了可以躲避风雨寒暑的房子。圣人又教人们制造农具和兵器，用来耕作和捕杀猛兽，使人们的生活比过去有了保障。后来，圣人又制礼作乐，订出各种各样的规矩，使人们有了礼节和约束。由此可见，社会是不断发展的，人们不是老是用一个方式生活。所以对古时候的制度，如果不再适合使用，就应该废除；而对于现在的，如果适合使用，就应该发扬。以上的一切都说明像千百条来自不同源头的江河，但最后都会归流入大海一样，各人做的事不同，但都是为了求得更好地治理社会，过更美好的生活。 ', ''],
            '百发百中': ['这故事记载在“史记”这本书中。战国时代，楚国有一个对射箭很精明的人，叫做养由基。养由基小就精通射箭，能够在一百步远的距离，命中那些只有三、四公分宽度的柳叶，同时，只要旁人指明想射中哪一片柳叶，他都能够很快的把箭射出，而且没有射不中的。因此，人人都夸赞他的箭法，有的人说“百步穿杨”，也有的人说“百发百中”，都是用来形容他射箭的绝技。它的意思是在称赞别人做事要有绝对的把握，有时分析事情，对将来的发展也一如所料。虽然现代的人们，已经很少人再对射箭会发生兴趣，但是“百发百中”这句成语，可以用在不只是箭术一件事情上，很多事情都可以引用。例如，喜欢玩手枪的人，他的射击技术很高明，他拔出手枪，并不需要花时间瞄准，就可以在射程的距离内准确的命中目标，这样，我们就可以说这个人的射击术“百发百中”。又譬如说某人对事物的发展，因为观察很仔细，并且了解它的规律，推断很正确，我们这个时候，也可以说他是“百发百中”。 ', ''],
            '百感交集': ['这个成语来源于《世说新语.言语》，卫洗马初欲渡江，形神惨悴，语左右云：“见此芒芒，不觉百端交集。苟未免有情，亦复谁能遣此！”卫獶，字叔宝，河东安邑（今山西夏县北）人，晋怀帝时任太子洗马（太子的侍从官）。他精读《易经》、《老子》，说话常常是非常深刻的西晋时期，统治集团内部矛盾重重。持续十六年之久的“八王之乱”给国家和人民造成了深重的灾难。北方的匈奴贵族刘裕乘机起兵入侵。晋怀帝永嘉三年（公元309年），匈奴军队两次长驱直入，一直打到西晋都城洛阳，但都被西晋军队击退。面对动荡不安的时局，卫獶决心把家迁往南方。他的哥哥卫在朝廷担任官职，母亲不忍心和卫ZAO分离，卫獶劝她要以家庭大计为重，终于说服母亲同意南迁。永嘉四年，卫獶告别哥哥，离开洛阳，带着母亲和妻子一起南下。卫獶一向体弱多病，一路上步途跋涉，餐风饮露，经受了千辛万苦。在将要渡长江的时候，他的神情容貌都显得憔悴不堪。他对左右的人说：“见到这白茫茫的江水，心里不由得百感交集。只要是一个有感情的人，又有谁能排遣这万千的思绪和感慨呢！”由于社会动荡，卫獶南迁也没有能够安居乐业。过江不久，妻子不幸亡故。他辗转到达建康（今江苏南京），于永嘉六年（公元312年）病逝，年仅二十七岁。 ', ''],
            '百丈竿头': ['宋朝时，长沙有位高僧名叫景岑，号招贤大师。这位太师佛学造诣高深，时常到各地去传道讲经。一天，招贤大师应邀到一座佛寺的法堂上讲经。前来听讲的僧人很多，大师讲得深入浅出，娓娓动听，听的人深受感染。法堂内除了大师的声音外，一片寂静。招贤大师讲经完毕后，一名僧人站立起来，问他行了一个礼，然后提了几个问题，请求大师解答。大师还了礼，慢慢地作答起来。那僧人听到不懂处，又向大师提问，于是两人一问一答，气氛亲切自然。听讲的人发现，他俩谈论的是有关佛教的最高境界----十方世界的内容。为了说明十方世界究竟是怎么回事，招贤大师当场出示了一份偈帖。所谓偈帖，就是佛教中记载唱词的本子。但见大师指着上面的一段文字念唱道：百丈的竹竿并不算高，尚需更进一步，十方世界才算是真正的高峰。', ''],
            '百折不挠': ['东汉官员桥玄品行端庄，嫉恶如仇。有次，一伙强盗绑住他十岁的儿子，带进他家，要正在病中的桥玄立即拿钱赎取，遭到桥直的怒斥。不多时，官兵包围了桥家，因怕强盗会杀桥直的儿子，迟迟不敢动手。这时桥玄愤怒地喊道：我难道能因为儿子的生命而放了这伙坏人吗？催促官兵们赶快动手。结果，桥玄的儿子被强盗杀死了。人们称赞桥玄百折不挠，始终保持节操。', ''],
            '败军之将': ['楚汉战争的时候，汉军大将韩信打垮了魏王豹后，继续攻打投靠楚军的赵王歇。但是他们必须经过一个叫井径的狭窄山口。赵王的谋臣李左车向赵王献计说：井径道路狭窄，汉军辎重一定拉在后面。我带一部分军队，抄小路去截断他们的辎重，就会使他们因失去给养而败走。可惜赵王没有采纳他的计策。韩信攻克赵后，向作为俘虏的李左车请教一些问题。李左车谦虚地推辞说：作为败军之将，我怎么可以教导你呢？这个成语意指打了败仗的将军。 ', ''],
            '班门弄斧': ['明朝有个文人叫梅之涣。有一回，他到采石矶（现在安徽当涂）唐代大诗人李白的墓地去游览，只见四周的墙壁上，涂涂抹抹全是游人写的诗，这些诗都很低劣。他也提起笔来写了一首：采石江边一堆土，李白之名垂千古。来来往往一首诗，鲁班门前弄大斧。这几句诗的意思是说李白是千古有名的诗人，而这些来来往往的人偏偏要在诗人面前炫耀自己，岂不就像在鲁班的门前耍弄斧头一样可笑吗！鲁班是春秋时期我国有名的巧匠。他聪明灵巧，有很多发明创造，是我国木匠、泥瓦匠的“祖师”，他的名字也就成了内行人的代称。成语“班门弄斧”就是从“鲁班门前弄大斧”一句变化来的，往往用来讽刺那种在内行人面前卖弄本领、不自量力的人，有时候也用来表示自谦。 ', ''],
            '半部论语': ['北宋著名的政治家赵普，原先是后周当节度使的赵匡胤手下的推官。公元960年，赵匡胤率军北上，部队到达陈桥时，赵普为赵匡胤出谋划策，发动兵变。赵匡胤黄袍加身，做了皇帝，改国号为宋，史称宋太祖。接着，赵普又辅佐宋太祖东征西讨，统一了全国。后来，宋太祖任命他为宰相。宋太祖死后，他的弟弟赵匡义继位，史称宋太宗。赵普仍然担任宰相。有人对宋太宗说赵普是山东人，不学无术，所读之书仅仅是儒家的一部经典《论语》而已，当宰相不恰当。宋太宗不以为然地说：“赵普读书不多，这我一向知道。但说他只读一部《论语》，我也是不相信的。”有一次宋太宗和赵普闲聊，宋太宗随便问道：“有人说你只读一部《论语》，这是真的吗？”赵普老老实实地回答说：“臣所知道的，确实不超出《论语》这部分。过去臣以半部《论语》辅助太祖平定天下，现在臣用半部《论语》辅助陛下，便天下太平。”后来赵普因为年老体衰病逝，家人打开他的书箧，里面果真只有一部《论语》。 ', ''],
            '半途而废': ['战国时期，有一个叫乐羊子的人，离开家到很远的地方去拜师学艺。一天，他的妻子正在家里织布，乐羊子突然回来了。他的妻子觉得奇怪，便问：你这么快就学完了？乐羊子说：没有，我在外面想家了，所以回来看看。他的妻子听了以后，拿起剪刀把一块已经织好的布剪成两段，然后对他说：这布是我辛辛苦苦、一点一点织出来的，现在我把它剪断了，就等于以前的时间和辛苦都白费了。你拜师求学，和我纺线织布是一样的！于是乐羊子离开家继续拜师求学去了。废：废止，停止。这个成语比喻事情做到一半停止不做了，不能坚持到底。', ''],
            '傍人门户': ['古时候，中国民间有一种风俗：过年时，用两块桃木板写上神仙的名字挂在门旁，以便压邪，这木板称作“桃符”；五月初五那天，将艾蒿扎成人形悬挂门户上方，用来驱赶毒气，称为“艾人”。有一天，桃符和艾人在一家的门上争吵起来。桃符抬头望着艾人骂道：“你这下贱的东西，怎么总是在我的头顶上！”艾人弯下身子说：“你的半截身子已经埋在土里了，还跟我争什么高低呢？”桃符听后，气得火冒三丈，同艾人争吵不休。这时，门神听得实在不耐烦了，出来调解说：“别吵了，我们都是没用的东西，正靠着别人的门户过日子，哪里还有闲工夫闹这种意气呢？”桃符和艾人听了门神的话，羞愧地垂下了头，不再争辩了。 ', ''],
            '包藏祸心': ['公元前541年，楚国的公子围在副手伍举的陪同下带了许多兵马到郑国去迎亲。原来，郑国是个小国，楚国是个大国，郑国与楚国交好，以便靠它的力量与别的诸侯国抗衡。为此，大夫公孙段把女儿嫁给楚国的公子围。执政大夫子产见公子围带了许多兵马来迎亲，担心他乘机侵袭，便不让公子围等住进城里的馆舍，并派子羽对公子围说：“敝都的馆舍狭小，容纳不下您这么多的随从，请就住在城外，并举行迎亲仪式吧。”公子围很不满意，命太宰伯州犁对子羽说：“承蒙贵君赐给敝君大夫恩惠，把贵君大夫的女儿嫁给敝君的大夫作妻子。敝国这次迎亲极为隆重，出发前摆了宴席，在宗庙中进行了祭告。如果在野外举行迎亲仪式，是把贵君的恩惠赐到草丛里去了，我们就欺骗了先君，不能再当大臣，也不能回去了。请大夫再考虑一下。”子羽说：“我们郑国国家小，但国小并没有罪过，倒是依靠大国而不设防备，那才是罪过。我们本想通过联姻使自己得到安宁，而楚国作为大国却怀着害人之心来打我们弱小的郑国的主意，这是行不通的。” ', ''],
            '抱残守缺': ['西汉时，有一个叫刘歆的人，字子骏，是著名学者刘向的儿子，曾拜为黄门郎（内廷侍从官）。后来与刘向共同掌管校勘和整理典籍，进行学术研究。在校勘工作中，他阅读了不少秘藏的古籍，发现了一本古文《春秋左氏传》，爱不释手。经过研究，刘歆认为，《左传》是一本珍贵的文献资料，便建议为《左传》等古籍建立学官。汉哀帝（刘欣）知道此事后，就命刘歆与五经博士讲论《左传》等一批古书的义理。但诸博士既不同意为《左传》等建立学官，又不肯讨论研究此事。刘歆对众博士的这种态度很气愤，给管博士的太常写了一封公文，对此提出了批评和抗议。刘歆的信中写到：这些博士不学无术，孤陋寡闻，怀着害怕别人识破他们的私意，没有服从真理的公心，所以抱残守缺，因循守旧，而不肯探求新的学问。由于刘歆的信言词痛切，引起了博士们的怨恨并因此遭受到了诽谤。后来，刘歆自请到地方做了个小官。根据这个故事，后人引伸出了“抱残守缺”这句成语，原意为守住陈旧、残破的东西，不肯放弃。现多用以比喻思想保守，不肯接受新事物。 ', ''],
            '抱薪救火': ['战国末年，秦国采取远交近攻的政策，不断并吞邻近的国家，好扩大自己的领土。其中，秦国曾经三次进攻魏国，占领魏国许多的土地，魏国军民也伤亡惨重。有一回，秦国又派乒攻打魏国，魏国于是请韩、赵两国援助，可惜兵力太弱，最后还是被打败。大将段干子提议把南阳割让给秦国求和，战略家苏代却持反对的意见，他说：秦国想并吞魏国，只割让土地是无法满足秦国的野心，就像抱着柴火去救火，柴没烧完，火是不会灭的。可是魏王不听苏代的劝阻，还是把南阳割让给秦国求和。最后真的就像苏代说的一样，秦国根本不满足，仍然继续攻打魏国，掠夺了魏国更多城池，最后弱小的魏国就被秦国消灭了。', ''],
            '杯弓蛇影': ['有一天，乐广请他的朋友在家里大厅中喝酒。那个朋友在喝酒的时候，突然看见自己的酒杯里，有一条小蛇的影子在晃动，他心里很厌恶，可还是把酒喝了下去。喝了之后，心里到底不自在，放心不下。回到家中就生起病来,隔了几天，乐广听到那个朋友生病的消息，了解了他得病的原因。乐广心里想：酒杯里绝对不会有蛇的！于是，他就跑到那天喝酒的地方去察看。原来，在大厅墙上，挂有一把漆了彩色的弓。那把弓的影子，恰巧映落在那朋友放过酒杯的地方，乐广就跑到那个朋友那里去，把这事解释给他听。这人明白了原因以后，病就立刻好了。后来人们就用杯弓蛇影比喻疑神疑鬼，自相惊扰。 ', ''],
            '杯水车薪': ['有一天傍晚，有个叫赵大的人砍柴回来路过一个茶馆，看见里面坐着很多人，有的在喝茶，有的在乘凉。赵大把拉柴的车停在外面，也走进了茶馆。他刚喝完一杯茶，就看见茶馆外面一片红光，饱到门口一看，原来是自已的一车柴草着火了，火苗直往上蹿。赵大一边大喊：不好了，着火啦，快救火啊！一边跑进茶馆，端起桌子上的一杯茶水往柴草上泼去。茶馆里的人听到喊声，也都端起茶杯往车上泼。可是火不但没灭，借助风势反而更大了。赵大揪住衣襟，垂头丧气地蹲在地上直叹气。', ''],
            '背道而驰': ['战国时代，魏国的臣子季梁，奉命出使到外国，可是他在路途中听到魏王准备要攻打赵国邯郸的消息，就赶紧回国去劝魏王。匆忙回国的季梁对魏王说：“我在太行山下，看到一个驾着车子的人，他赶着马想要去北边，说他准备到楚国去。”魏王说：“楚国应该是向南走的，为什么他要往北走呢？”季梁回答说：“我也这么跟他说的啊！可是，他认为他的马是匹好马，速度非常快，加上他也带了足够的钱；而且车夫经验丰富，所以他觉得没有什么好担心的。因此，他不听我的劝告，就继续往北走了。”魏王听了之后，哈哈大笑说：“这个人是个疯子。虽然他有很多好的条件，但是他却往反方向走，怎么可能到得了目的地呢。”接着季梁就告诉魏王说：“大王说的话一点也没错。但是，像大王现在这样一直攻打附近的国家，这种举动也会让大王离称霸的目标越来越远，这不也是和那个往反方向去走的人一样吗？” ', ''],
            '背水一战': ['韩信，淮阴（今江苏清江西南）人。他是汉王刘邦手下的大将。为了打败项羽，夺取天下，他为刘邦定计，先攻取了关中，然后东渡黄河，打败并俘虏了背叛刘邦、听命于项羽的魏王豹，接着往东攻打赵王歇。韩信的部队要通过一道极狭的山口，叫井陉口。赵王手下的谋士李左军主张一面堵住井陉口，一面派兵抄小路切断汉军的辎重粮草，韩信的远征部队没有后援，就一定会败走；但大将陈余不听，仗着兵力优势，坚持要与汉军正面作战。韩信了解到这一情况，非常高兴。他命令部队在离井陉三十里的地方安营，到了半夜，让将士们吃些点心，告诉他们打了胜仗再吃饱饭。随后，他派出两千轻骑从小路隐蔽前进，要他们在赵军离开营地后迅速冲入赵军营地，换上汉军旗号；又派一万军队故意背靠河水排列阵势来引诱赵军。到了天明，韩信率军发动进攻，双方展开激战。不一会，汉军假意败回水边阵地，赵军全部离开营地，前来追击。这时，韩信命令主力部队出击，背水结阵的士兵因为没有退路，也回身猛扑敌军。赵军无法取胜，正要回营，忽然营中已插遍了汉军旗帜，于是四散奔逃。汉军乘胜追击，打了一个大胜仗。在庆祝胜利的时候，将领们问韩信：兵法上说，列阵可以背靠山，前面可以临水泽，现在您让我们背靠水排阵，还说打败赵军再饱饱地吃一顿，我们当时不相信，然而竟然取胜了，这是一种什么策略呢？韩信笑着说：这也是兵法上有的，只是你们没有注意到罢了。兵法上不是说‘陷之死地而后生，置之亡地而后存’吗？如果是有退路的地方，士兵都逃散了，怎么能让他们拼命呢！这个故事演化出成语背水一战，多用于军事行动，也可用于比哺有决战性质的行动。', ''],
            '本末倒置': ['战国时，有一次齐国的国王派使臣去访问赵国。使臣到了赵国，把齐王的信交给了赵威王，赵威王连看都没看，就亲切地问使臣：齐国怎么样？今年收成好吗？老百姓生活得好吗？齐王的身体好吗？使臣听了，心里很不高兴，对赵威王说：齐王派我来访问赵国，可您连信都不看，而是先问收成、百姓，最后才问国王，这不是本末倒置吗？赵威王笑着说：对于一个国家来讲，粮食是最重要的，还有，如果没有百姓，哪有什么国王啊！所以我这样问，根本没有本末倒置。本末：树根和树梢，比喻事物的根本和细枝末节；置：放置。这个成语比喻把主要的和次要的，根本的和非根本的的关系搞颠倒了。 ', ''],
            '逼上梁山': ['水浒传》中有一个梁山英雄，名叫林冲，原来是80万禁军教头。有一天，林冲带着妻子去赶庙会，没想到俩人走散了。太尉高俅的干儿子高衙内看见林冲的妻子长得漂亮，就起了坏心。正在这时，林冲赶到了，他见妻子被人欺负，非常气愤，就在举起拳头要打时，才看清是高衙内，就忍气吞声地回了家。谁知高衙内为了霸占林冲的妻子，玩弄手法陷害林冲，还派人在流放的路上杀害林冲。林冲被逼得无路可走，只得上梁山造反。梁山：地名，在今山东省梁山县。这个成语比喻被迫反抗或做某件事。 ', ''],
            '比肩接踵': ['楚灵王知道晏婴长得矮小，就和大臣们定计，想戏辱他。晏婴到了楚国郢都，可是城门紧闭。一个楚国的卫兵把晏婴领到一扇新开的小门前，请他从小门进城。晏婴冷笑一声，说：这是狗洞，出使狗国从这儿进；我出使楚国，怎能从这里进！楚灵王反被晏子戏辱，只得大开城门，迎晏婴进城。楚灵王还想戏弄晏婴，在接见时，第一句话就问：难道齐国没有人了吗？晏婴大声回答：我国京城行人比肩接踵，怎么说没有人？楚灵王笑着说：既然有人，为什么叫你这个矮子出使我国呢？晏婴叹口气说：我国那些体面能干的使臣，到有贤君的国家去了。晏婴加重语气说：像我这样无用的人，只好来见你了。比肩接踵成语由此而来。肩并肩，脚尖靠着脚跟，形容人多拥挤。 ', ''],
            '必恭必敬': ['周幽王姬宫涅是西周的最后一个国君，他昏庸暴虐，政治腐败。公元前779年，褒国进献了一个姓姒的美女，叫褒姒。周幽王十分宠爱她。褒姒一向不爱笑，幽王用音乐歌舞、美味佳肴都不能让她笑。有人献计点燃报警的烽火台，召来各路诸侯兵马，使他们上当，让褒姒笑一笑，幽王欣然同意。他带褒姒到行宫游玩，晚上传令点燃烽烟，各地诸侯见到烽烟，以为有盗寇侵扰京城，纷纷率领兵马赶来相救。到了一看，只见幽王在喝酒取乐。幽王派人对他们说：“没有什么盗寇，让你们辛苦了！”诸侯受骗，匆匆地来，匆匆地去。褒姒看了不由大笑，幽王也很开心。褒姒生了个儿子叫伯服，幽王废掉申后，立褒姒为王后；废掉申后生的太子宜臼，立伯服为太子。宜臼遭到废黜，住在外祖父申侯家里。他对自己的命运和国家的前途，满怀忧愁，心中十分痛苦，写了一首题目叫作《小弁》的诗，抒发自已的心情。诗的第三节说：“看见屋边的桑树和梓树，一定要必恭必敬。我尊敬的是自己的父亲，我依恋的是自己的母亲。谁人不是父母的骨肉，谁人不是父母所生？上天生了我，可我的好日子到何处找寻？”由于幽王无道，诸侯纷纷叛离。公元前771年，宜臼的外祖父申侯联合犬戎的军队进攻镐京。幽王下令点燃烽烟，但是诸侯受过骗，都不派救兵。犬戎的军队攻下镐京，杀了幽王，掳走了褒姒。', ''],
            '毕恭毕敬': ['周幽王姬宫涅是西周的最后一个国君，他昏庸暴虐，政治腐败。公元前779年，褒国进献了一个姓姒的美女，叫褒姒。周幽王十分宠爱她。褒姒一向不爱笑，幽王用音乐歌舞、美味佳肴都不能让她笑。有人献计点燃报警的烽火台，召来各路诸侯兵马，使他们上当，让褒姒笑一笑，幽王欣然同意。他带褒姒到行宫游玩，晚上传令点燃烽烟，各地诸侯见到烽烟，以为有盗寇侵扰京城，纷纷率领兵马赶来相救。到了一看，只见幽王在喝酒取乐。幽王派人对他们说：没有什么盗寇，让你们辛苦了！诸侯受骗，匆匆地来，匆匆地去。褒姒看了不由大笑，幽王也很开心。褒姒生了个儿子叫伯服，幽王废掉申后，立褒姒为王后；废掉申后生的太子宜臼，立伯服为太子宜臼遭到废黜，住在外祖父申侯家里。他对自己的命运和国家的前途，满怀忧愁，心中十分痛苦，写了一首题目叫作《小弁》的诗，抒发自已的心情。诗的第三节说：看见屋边的桑树和梓树，一定要必恭必敬。我尊敬的是自己的父亲，我依恋的是自己的母亲。谁人不是父母的骨肉，谁人不是父母所生？上天生了我，可我的好日子到何处找寻？由于幽王无道，诸侯纷纷叛离。公元前771年，宜臼的外祖父申侯联合犬戎的军队进攻镐京。幽王下令点燃烽烟，但是诸侯受过骗，都不派救兵。犬戎的军队攻下镐京，杀了幽王，掳走了褒姒。', ''],
            '筚路蓝缕': ['春秋时，小小郑国，地处晋、楚两大国之间。北方的晋国和南方的楚国，为了争夺郑国，矛盾很大。郑国既害怕楚国，也不敢得罪晋国，处境十分为难。《左传·宣公十二年》记载：那年春天，楚国攻打郑国，郑国抵挡不住，只得向楚国求和。晋国得到消息，立刻派兵抗楚救郑，目的是要把郑国争取过来，使他归附晋国。可是晋军还没渡过黄河，郑国已经屈服，楚军也准备胜利回师了。晋军的中军主将荀林父等部分将领，便主张停止进军。而中军副将先縀和另一部分将领却不同意，于是发生了争执。晋军暂驻在敖、郱二山之间。郑国派人到晋军营中去声明：“我们郑国向楚国求和，不过是为了不致亡国，丝毫也没有对晋国不友好的意思。”还说：“楚军轻而易举地得了胜利，因此骄傲了，部队也放松戒备了。你们如果趁此追击，加上我们从旁助战，定可把楚军打得大败。”先縀高兴地说：“对呀，打败楚军，夺回郑国，正是时候了！”下军副将栾书说：“不行，楚国经常教诫全国军民，要发扬他们祖先‘筚路蓝缕，以启山林’的精神，勤俭建国，艰苦奋斗。有什么理由说他们骄傲了，放松戒备了？况且郑国劝我们攻打楚军，其实也并不是真心向着我们。要是我们打胜了，他固然会讨好我们，要是楚军打胜了，他还不是又要向楚国投降。我们怎么可以相信郑国的话呢？”上述栾书这段话中“筚路蓝缕，以启山林”是什么意思呢？筚，是荆、竹、树枝之类；路，同“辂”，就是大车。筚路，是用荆竹树枝等编制成的大车，或者叫做柴车；蓝缕，即“褴褛”，破烂的衣服。启，就是开。这句话是说，驾着柴车，穿着破衣，去开发荒山野林。相传楚国当初就是以这样的精神创建起来的。', ''],
            '髀肉复生': ['“髀肉复生”这则成语的意思是比喻长久处于安逸环境中虚度光阴，忧虑不能再有所作为。这个成语来源于《三国志.蜀书.先左传》，备曰：“吾常身不离鞍，髀肉皆消。今不复骑，髀里肉生。日月若驰，老将至矣，而功业不建，是以悲耳。”刘备在与曹操作战中失败后，丧失了地盘，只得投奔汉皇族刘表。一天，刘表请刘备喝酒聊天。席间，刘表对刘备说：“上次没有听您的话，失去了一个好机会，真可惜！”刘备安慰地说：“如今天下分裂，天天有战事。上次失去机会，怎么知道今后不能再碰到呢！机会是没有尽头的。已经过去的事，就不必再后悔了。”两人交谈得很投机，又商量了以后的打算。过了一会儿，刘备起身上厕所，他摸了摸自已的髀（大腿），发现上面的肉又长起来了，不禁掉下泪来。回到座上的时候，脸上还留着泪痕。刘表见了很奇怪，问他道：“怎么啦？您是不舒服还是有什么心事？”刘备不好意思地说：“没什么，实说吧。我以前一直南征北战，长期身子不离马鞍，大腿上的肉精壮结实，到这里来后，一晃就是五年，闲居安逸，用不着骑马，髀上的肉复长，又肥又松。一想起时光过得这么快，人都快老了，复兴汉室的功业一点也没有建成，因此心里非常难受。” ', ''],
            '鞭长莫及': ['这个成语来源于《左传.宣公十五年》，宋人使乐婴齐告急于晋。晋侯欲救之，伯宗曰：“不可。古人有言曰：‘虽鞭之长，不及马腹。’天方授楚，未可与争，虽晋之强，能违天乎！”鲁宣公十四年（公元前595年），楚庄王派申舟出使齐国。出使路上要经过宋国，楚庄王仗着国力强盛，要申舟不向宋国借路。申舟说：“如果不借路，宋国人会杀我。”“宋国要是杀了你，我就派兵攻打他们。”楚庄王说。果然，不向宋国借路的做法激怒了宋国。宋国君臣认为这是对本国的莫大侮辱，就杀了申舟。楚庄王听到这个消息，气得暴跳如雷，立即发兵攻打宋国，一下子就把宋国的都城团团围住。双方相持了几个月，楚军还是没有取胜。第二年春天，宋国派大夫乐婴齐到晋国去请求晋国派兵救援。晋景公想要发兵去救宋，国大夫伯宗说：“大王，我们不能出兵，古人有话说：‘鞭子虽然长不能打到马肚于上。’现在楚国强盛，正受到上天保佑，我们不能和楚相争。晋国虽然强大，可是能违反天意吗？俗话说：‘高高低低，都在心里’，江河湖泊中容纳有污泥浊水，山林草丛中暗藏有毒虫猛兽，洁白的美玉中隐藏有斑痕，晋国忍受一点耻辱，这也是很正常的事。您还是忍一忍吧。”景公听了伯宗的话，停止发兵，改派大夫解扬去宋国，叫宋国不要投降，就说援兵已经出发，很快就要到了。宋国人在城中极其艰苦地坚守了几个月，楚军攻打不下，最后同意宋国求和，并带走宋国大夫华元作为人质。', ''],
            '标新立异': ['这个成语来源于《世说新语·文字》：《庄子·逍遥》篇，旧是难处，诸名贤所不可钻味，而不能拔理于郭、向之外。支道林在白马寺中将冯太常共语，因及《逍遥》，支卓然标新理于二家之表，立异义于众贤之外，皆是诸名贤寻味之所不得。支道林，名遁，是东晋时的佛教学者，本姓关，陈留（今河南开封南）人。他常与谢安、王羲之等名士交往，喜欢谈玄理，对《庄子》也很有研究。《庄子》是战国时期庄周所着的一部哲学著作。晋代的向季曾为《庄子》作注，没有完成就死了，郭象继续他的工作，完成了注释，后来人们都引用郭象和向秀所作的注。《逍遥游》是《庄子》中的第一篇，也是一个难点。当时许多著名的学者深入钻研体味这篇文章的道理，都没有能够超出郭象、向秀的见解。有一次，支道林在洛阳白马寺同太常护国将军冯怀一起聊天，谈到《逍遥游》，支道林说出了一种新的道理，大大高于郭象、向秀的解释，树立了一种新的见解，超出当时许多著名学者的认识。支道林所作的分析见解，都是那些著名学者苦苦搜求思索没有能够解决的。后来人们就吸收了支道林的意见来解释《逍遥游》。', ''],
            '别开生面': ['唐朝初年，唐太宗为了表彰２４位开国功臣，命人在皇宫凌烟阁里面上这些人的肖像。70多年后，这些画像的颜色都已黯淡了。唐玄宗听说曹操的后代曹霸擅长画人物和马匹，就命他重新设色描摹，使24位功臣重现光彩，玄宗看后非常高兴，下诏封曹霸为左武卫将军。安史之乱后，曹霸流落到成都，靠卖画度日。诗人杜甫听说后，找到曹霸，写了一首《丹青引·赠曹将军霸》：凌烟功臣少颜色，将军下笔开生面。．．．．．．以表深切的同情。 ', ''],
            '别无长物': ['这个成语来源于《晋书.王恭传》，恭曰：吾平生无长物。东晋时有个读书人，名叫王恭。他生活俭朴，不图享受，人们都说他将来定能做一个有用的人。有一年，王恭随父亲从会稽来到都城建康，他的同族王忱去看望他，两人在一张竹席上促膝谈心。谈着谈着，王忱忽然觉得身下的席子非常光滑，感到很舒服。他心想王恭从盛产竹子的会稽来，一定带了不少这样的竹席，就称赞了一番这张竹席，并希望王恭能送他一张竹席。王恭听了，毫不犹豫地将身下这张竹席赠送给王忱。王忱千恩万谢地走了。其实，王恭只有这张竹席。送掉后，他就改用了草席。王忱知道这情况后，十分惊讶，觉得过意不去，就去找王忝表示歉意。王恭笑笑说：您不太了解我，我王恭平生没有什么多余的物品。 ', ''],
            '别有天地': ['这个成语来源于《李太白全集.山中问答》，问余何意栖碧山，笑而不答心自闲。桃花流水杳然去，别有天地非人间。李白，字太白，自号背莲居士，是我国唐代最伟大的诗人之一。他的祖籍是陇西成纪（今甘肃天水附近），先世因罪迁居西域，出生在碎叶（今独联体境内），在绵州（今四川绵阳）的青莲乡长大。李白年轻的时候，爱好剑术，轻财仗义，善于作诗。25岁那年，他身佩宝剑，辞别亲人，离开故乡，出外远游。几年间，漫游了现湖南、湖北、江苏、浙江的许多地方。他才能出众，抱负远大，渴望参加政治活动，但是在黑暗的官场里，他光明磊落的胸怀和正直不屈的性格是不受欢迎的，所以十多年没有结果。四十一岁那一年，李白受到唐玄宗召见，他的才能在京中轰动一时。但当时的唐玄宗是个一心追求享乐的“太平天子”，国家政务操纵在奸相李林甫和宦官高力士手中。唐玄宗只希望李白做一个歌功颂德的御用文人。但李白性情孤傲，在皇帝和权贵面前没有丝毫媚态，因而遭到高力士等人的诽谤，逐渐不受唐玄宗信任,当李白看清唐玄宗确实没有重用自己的意思之后，他担心会因小人的诽谤而遭祸害，就自动要求离开朝廷。在长安的三年生活中，他认清了现实的黑暗和统治者的腐败，写出了许多有深刻思想内容的诗篇。离开长安之后，李白又开始了十年的漫游生活。由于在现实生活中屡遭挫折，他产生了求仙访道的想法，希望摆脱丑恶的现实追求美好生活。《山中问答》就是他写的一首追求美好境界的诗，诗意是这样的：有人问我为什么栖宿在碧山，我微笑着没有回答，心中自在悠闲。且看那桃花随着流水自由自在地飘向远方，这里另有一种境界，不同于黑暗、污浊的人间。', ''],
            '宾至如归': ['春秋时，郑国子产奉郑简公之命，出访晋国。晋平公摆出大国架子，没有迎接他。子产就命令随行人员把晋国的宾馆围墙拆掉，把车马开进去。晋国大夫士文伯责备子产说道：我国为保证诸侯来宾的安全，所以修了宾馆，筑了高墙。现在你们把墙拆了，来宾的安全由谁负责？子产回答说道：我们郑国小，所以要按时前来进贡。这次贵国国君没有空闲接见我们。我们带来的礼物既不敢冒昧献上，又不敢让这些礼物日晒夜露。我听说从前晋文公做盟主时，接待诸侯来宾并不这样。那时宾馆宽敞漂亮，诸侯来了，像到家里一样。而今，你们的离宫宽广，宾馆却像奴隶住的小屋，门囗窄小，连车子都进不去：客人来了不知什么时候才能被接见。这不是有意叫我们为难吗？士文伯回去向晋平公报告。晋平公自知理亏，便向子产认错道歉，并立刻下令兴工，重修宾馆。客人像回到自己的家一样，形容客人受到很好的招待。 ', ''],
            '冰山难靠': ['唐玄宗李隆基特别宠爱杨玉环，封她为贵妃。这下杨家便鸡犬升天了，她的堂兄杨国忠也官运亨通做了宰相，还兼领四十余个使官，大权在握，朝廷选任官吏都在他家里私下决定。当时，陕西有一个进士，名叫张彖没有机会作官。他的朋友们都劝他去拜见杨国忠，那样立刻就能升官发财。可是他始终不去，反倒对劝他的朋友说：“你们都把杨国忠看得像泰山一样稳固，可是我以为他不过是一座冰山罢了。将来天下有了动乱，他就会垮掉，好比冰山遇到太阳化掉一样，到那时候你们就失掉靠山了。”不久，安禄山起兵叛乱，攻下京城长安，杨国忠随同唐玄宗逃往四川，在马嵬驿，被士兵杀死。杨贵妃也被缢死，杨家这座靠山果然塌倒了。 ', ''],
            '兵不血刃': ['东晋的屯骑校尉郭默作战勇敢，曾与后赵的建立者石勒等作过战，石勒等都很怕他。但此人一贯骄横跋扈，把谁都不放在眼里，有一次因为泄私愤竟然杀死了平南将军刘胤。事后，还大胆伪造诏书，诬谄刘胤谋反，向各州郡通报。这件事暴露后宰相王导怕朝廷无力惩处他，不但不向他问罪，反而加封他的官职。陶侃知道这件事后，一方面上书朝廷请求讨伐郭默，一方面写信给王导，要求他采取果断措施。信中有两句话写得非常有力：“郭默杀害州官，朝廷就任命他当州官。难道他杀害宰相，也就让他当宰相不成！”王导读了这封信，受到很大的触动，便派陶侃率军去讨伐郭默。郭默深知陶侃领兵作战十分厉害，听说他亲自来讨伐，非常焦急，打算率军离开江州南下。但陶侃出兵神速，郭默还未离城，陶侃的大军就已经将江州团团围住。郭默想固守城池，但又知道自已不是陶侃对手，怕城破后难逃性命；想开城门投降，又怕朝廷要杀他的头，真是左右为难。他手下的一名叛将见大势已去，将他逮捕后开城门投降。陶侃终于不战而取得胜利，平定了这次叛乱。', ''],
            '兵不厌诈': ['公元前633年，楚国攻打宋国，宋国向晋国求救。第二年春天，晋文公派兵攻占了楚的盟国曹国和卫国，要他们与楚国绝交，才让他们复国。楚国被激怒了，撤掉对宋国的包围，来和晋国交战。两军在城濮（今山东鄄城西南）对阵。晋文公重耳做公子时，受后母迫害，逃到楚国，受到楚成王的款待。楚成王问重耳以后如何报答，重耳说：“美女、绸缎等等，您都有了，我能给您什么呢？假如托您的福我能回国执政，万一遇到两国发生战争，我就撤退三舍（舍为十里）。如果楚国还不能谅解，双方再交手。”为了实现当年的诺言，晋文公下令撤退九十里。楚国大将子玉率领楚军紧逼不舍。当时，楚国联合了陈、蔡等国，兵力强；晋国联合了齐、宋等国，兵力弱。应该怎样作战呢？晋文公的舅舅子犯说：“我听到过这样的说法：对于注意礼仪的君子，应当多讲忠诚和信用，取得对方信任，在你死我活的战阵之间，不妨多用欺诈的手段迷惑对方。你可以采取欺骗敌军的办法。”晋文公听从了子犯的策略，首先击溃由陈、蔡军队组成的楚军右翼，然后主力假装撤退，引诱楚军左翼追赶，再以伏兵夹击。楚军左翼大败，中军也被迫撤退。这就是历史上著名的以弱胜强的城濮之战。晋国取胜后，与齐、鲁、宋、郑、蔡、莒、卫等国会盟，成为诸侯霸主。在这个故事中，还引申出另一个成语“退避三舍”，用来比喻退让或回避，避免发生冲突。', ''],
            '兵贵神速': ['郭嘉，字奉孝，颍川阳翟（今河南禹县）人。他足智多谋，受到曹操的信任和重用。曹操打败了据有冀、青、幽、并四州的袁绍，杀了袁绍长子袁谭，袁绍的另外两个儿子袁尚、袁熙逃走，投奔辽河流域的乌丸族首领蹋顿单于。蹋顿乘机侵扰汉朝边境，破坏边境地区人民的正常生产和生活。曹操有心要去征讨袁尚及蹋顿，侣有些官员担心远征之后，荆州的刘表会乘机派刘备来袭击曹操的后方。郭嘉分析了当时的形，对曹操说：“你现在威镇天下，但乌丸仗着地处在边远地区，必然不会防备。进行突然袭击，一定能消灭他们。如果延误时机，让袁尚、袁熙喘过气来，重新收集残部，乌丸各族响应，蹋顿有了野心，只怕冀州、青州又要不属于我们了。刘表是个空谈家，知道自己才能不及刘备，不会重用刘备，刘备不受重用，也不肯多为刘表出力。所以你只管放心远征乌丸，不会有后顾之忧的。”曹操于是率领军队出征。到达易县（今属河北）后，郭嘉又对曹操说：“用兵贵在神速。现在到千里之外的地方作战，军用物资多，行军速度就慢，如果乌丸人知道我军的情况，就会有所准备。不如留下笨重的军械物资，部队轻装，以加倍的速度前进，乘敌人没有防备发起进攻，那就能大获全胜。”曹操依郭嘉的计策办，部队快速行军，直达蹋顿单于驻地。乌丸人惊慌失措地应战，一败涂地。蹋顿被杀，袁尚、袁熙逃往辽东后被太守孙康所杀。 ', ''],
            '病入膏肓': ['春秋时，晋景公患了重病，派人到秦国请名医来医治。他在病床上梦见两个小孩，其中一个说：不好了，病人要请名医来了，咱们要遭祸的，快逃吧！另一个说：别怕，咱们躲到膏之下，盲之上，不管什么样的医生，用啥药，都把我们不能怎么样。景公醒来，觉得有些奇怪。心想，难道那两个小孩就是病魔？过了一会，秦国的医生来了，诊断后说：没办法了，你的病已经在膏肓，药力达不到那里，治不了啦。膏肓：古人把心尖脂肪叫膏；心脏和隔膜之间叫盲。这个成语形容病情严重到无法医治的地步，也比喻事态严重到不可挽救的地步。 ', ''],
            '波澜老成': ['元朝汤编著的《画鉴·宋画》里记载着一个故事。宋朝有个名叫徐友的画家，有一次在常州太和寺佛殿后面的墙壁上，画了一幅描绘河水的壁画，题名《清济贯河》，其中有一笔从头到尾长达40丈，受到观众的特别注意。汤对此发表评论说：“其实徐友的妙处并不在此。因为他功力深厚，笔法老练，线条连绵不断，像波涛起伏（原文是‘笔法既老，波澜起伏’），跟水势相结合，互相影响，就觉得越看越奇了。”', ''],
            '伯乐相马': ['传说天上管理马匹的神仙叫伯乐。在人间，人们把精于鉴别马匹优劣的人也称为伯乐。第一个被称作伯乐的人本名孙阳，他是春秋时代的人。由于他对马的研究非常出色，人们便忘记了他本来的名字，干脆称他为伯乐，一直到现在。一次，伯乐受楚王的委托，购买能日行千里的骏马。伯乐向楚王说明，千里马少有，找起来不容易，需要到各地巡访，请楚王不必着急，他尽力将事情办好。伯乐跑了好几个国家，仔细寻访盛产名马的燕赵一带，辛苦倍至，但还是没发现中意的良马。一天，伯乐从齐国返回，在路上，看到一匹马拉着盐车，很吃力地在陡坡上行进。马累得呼呼喘气，每迈一步都十分艰难。伯乐对马向来亲近，不由走到跟前。马见伯乐走近，突然昂起头来瞪大眼睛，大声嘶鸣，好象要对伯乐倾诉什么。伯乐立刻从声音中判断出，这是一匹难得的骏马。伯乐对驾车的人说：这匹马在疆场上驰骋，任何马都比不过它；但用来拉车，它却不如普通的马。你还是把它卖给我吧。驾车人认为伯乐是个大傻瓜，他觉得这匹马太普通了，拉车没气力，吃得太多，又骨瘦如柴，于是毫不犹豫地同意了。伯乐牵走千里马，直奔楚国。伯乐牵马来到楚王宫，拍拍马的脖颈说：我给你找到了好主人。千里马像明白伯乐的意思，抬起前蹄把地面震得咯咯作响，引颈长嘶，声音洪亮，如大钟石盘，直上云霄。楚王听到马嘶声，走出宫外。伯乐指着马说：大王，我把千里马给您带来了，请仔细观看。楚王一见伯乐牵的马瘦得不成样子，认为伯乐愚弄他，有点不高兴，说：我相信你会看马，才让你买马，可你买的是什么马呀，这马连走路都很困难，能上战场吗？伯乐说：这确实是匹千里马，不过拉了一段车，又喂养不精心，所以看起来很瘦。只要精心喂养，不出半个月，一定会恢复体力。楚王一听，有点将信将疑，便命马夫尽心尽力把马喂好，果然，马变得精壮神骏。楚王跨马扬鞭，但觉两耳生风，喘息的功夫，已跑出百里之外。后来千里马为楚王驰骋沙场立下不少功劳。楚王对伯乐更加敬重了。 ', ''],
            '博而不精': ['东汉著名的经学家郑兴，以研究《左氏春秋》着称于世。他的儿子郑众，十二岁时就跟父亲学习这部经学著作。后来，郑众还学习了《周易》，《毛诗》，《周礼》等经学著作，使他学识渊博，几乎无所不晓，在上层社会很有名气。郑众当官后，在公务之余给一些年轻人讲解《毛诗》、《周礼》等经学著作，并且花很大的精力为《左氏春秋》作注。后来，终于完成了《左氏春秋》的注释工作。这部书流传后，和另一位经学家贾逵所注的《左氏春秋》齐名，都受到学者们的好评。当时，最著名的经学家是马融。他注过《周易》、《尚书》、《毛诗》、《三礼》、《论语》、《孝经》，使古文经学达到成熟的境地，因此，弟子多达千人。马融除了为经书作注外，又兼注《老子》、《淮南子》。讲课时坐在高堂上，挂上纱帐，前面让学生坐着听课，后面列一班女乐演奏音乐，很有特点。马融研究了《左传》后，也准备注一部《左氏春秋》，他仔细阅读了贾逵和郑众的注本后评价说：“贾逵的注本精深而不广博，郑众的注本广博而不精深。要是既精深又广博，那我怎能超过他们？”马融觉得，这两个注本各有各的长处，合起来就弥补了各自的不足之处，便决定不再给《左氏春秋》作注了。 ', ''],
            '博士买驴': ['北齐的文学家颜之推，着成一部《颜氏家训》。在《颜氏家训》的《勉学》篇中，记载了一则博士买驴的笑话，这是他到邺城去办事时听到的。当时有个博士，熟读四书五经，满肚子都是经文。他非常欣赏自己，做什么事都要咬文嚼字一番。有一天，博士家的一头驴子死了，就到市场上去买一头。双方讲好价后，博士要卖驴的写一份凭据。卖驴的表示自己不识字，请博士代写，博士马上答应。卖驴的当即借来笔墨纸砚，博士马上书写起来。他写得非常认真，过了好长时间，三张纸上都是密密麻麻的字，才算写成。卖驴的请博士念给他听，博士干咳了一声，就摇头晃脑地念了起来，过路人都围上来听。过了好半天，博士才念完凭据。卖驴的听后，不理解地问他说：“先生写了满满三张纸，怎么连个驴字也没有呀？其实，只要写上某月某日我卖给你一头驴子，收了你多少钱，也就完了，为什么唠唠叨叨地写这么多呢？”在旁观看的人听了，都哄笑起来。这件事传开后，有人编了几句讽刺性的谚语：“博士买驴，书卷三纸，未有驴字。”', ''],
            '卜昼卜夜': ['敬仲，即春秋时陈国的公子完，同陈宣公是兄弟。陈宣公为了叫宠姬所生的儿子款为太子，便把原来立为太子的大儿子御寇杀了。敬仲是站在御寇一边的，因此不能在陈国安身立足，便投奔齐国。齐桓公很恭敬地接待敬仲，拜他为“卿”。敬仲谦虚地说：“我是投奔贵国的客人，蒙您收留，让我在这里舒舒服服地住下，我已经非常感激了，怎敢高居卿位，让人笑我不知足呢！”齐桓公觉得他很懂道理，便改聘为“工正”，请他担任管理各种工匠的职务。但是对他的待遇，仍不同于一般官员。齐桓公经常找他谈天、游玩。这段故事，在《左传·庄公二十二年》有记载。同时，它还记载着这么一件有趣的事情：有一次，齐桓公到敬仲家里去，敬仲拿出酒来招待他，桓公喝得很高兴，直到天快黑了，还叫点灯，要继续喝。敬仲婉言劝止，说道：“臣卜其昼，未卜其夜，不敢！（我只准备白天陪您玩，却没有打算继续到夜晚，恕我不敢久留您！）”由于这段故事，后来形容游宴无度，不计时间，从白昼到黑夜，又从黑夜到白昼，连续不休地玩乐，就叫“卜昼卜夜”。', ''],
            '补天浴日': ['上古时代，有一次，水神共工和火神祝融大战。共工大败，气得向西方不周山一头撞去，把不周山撞坏了。不周山是撑天的大柱，大柱一断，天就坍塌了一大块，地也陷裂了很多；同时，山林起火，洪水横流，世界发生了可怕的灾难。创造世界万物的女神娲（女娲是邯郸市涉县人，娲皇宫就坐落在涉县境内），在大江大河中挑选了许多五彩的石子，架起火来，把石子炼成熔液，然后用这种熔液去修补破坏了的天。她又杀了一只大得无法形容的乌龟，斩下它的４脚，作为４根天柱，竖立在四方，把天撑住。还利用大火后遗留的芦草灰，堵住了洪水。一场大难，始告平息。太阳女神羲和，生有10个儿子，也就是10个太阳。他们住在东方海外的汤谷。那里有一棵大树，名叫“扶桑”，所以那地名也叫“扶桑”。这棵大树有几千丈高，10个太阳，就住在这棵大树上。他们每天一个，轮流在天空值班。早上，不论哪个太阳值班，都由他们的妈妈羲和架车伴送。这辆车子很壮观，是由６条龙拉着的。从起点汤谷到终点蒙谷，共有16个站，正好一天的路程。车到第14站悲泉，太阳就得下车步行，妈妈羲和架着空车赶回汤谷，为伴送明天值班的儿子去作准备。每天早上，值班的太阳离开扶桑，登上龙车之前，一定先要在咸池里洗一个澡。羲和还常常带着儿子们在东南海外的甘渊一块洗澡，甘渊的水，十分甘美，羲和把儿子们一个个都洗得干干净净，明明亮亮。', ''],
            '捕风捉影': ['谷永，字子云，长安（在今陕西西安市）人，汉成帝时担任过光禄大夫、大司农等职。汉成帝二十岁做皇帝，到四十多岁还没有孩子。他听信方士的话，热衷于祭祀鬼神。许多向汉成帝上书谈论祭祀鬼神或谈论仙道的人，都轻而易举地得到高官厚禄。成帝听信他们的话，在长安郊外的上林苑大搞祭祀，祈求上天赐福，花了很大的费用，但并没有什么效验。谷永向汉成帝上书说：“我听说对于明了天地本性的人，不可能用神怪去迷惑他；懂得世上万物之理的人，不可能受行为不正的人蒙蔽。现在有些人大谈神仙鬼怪，宣扬祭祀的方法，还说什么世上有仙人，服不死的药，寿高得像南山一样。听他们的说话，满耳都是美好的景象，好象马上就能遇见神仙一样；可是，你要寻找它，却虚无缥缈，好象要缚住风、捉住影子一样不可能得到。所以古代贤明的君王不听这些话，圣人绝对不说这种话。”谷永又举例说：周代史官苌弘想要用祭祀鬼神的办法帮助周灵王，让天下诸侯来朝会，可是周王室更加衰败，诸侯反叛的更多；楚怀王隆重祭祀鬼神，求神灵保佑打退秦国军队，结果仗打败了，土地被秦削割，自己做了俘虏；秦始皇统一天下后，派徐福率童男童女下海求仙采药，结果一去不回，遭到天下人的怨恨。最后，他又说道：“从古到今，帝王们凭着尊贵的地位、众多的财物，寻遍天下去求神灵、仙人，经过了多少岁月，却没有丝毫应验。希望您不要再让那些行为不正的人干预朝廷的事。”汉成帝认为谷水说得很有道理，便听从了他的意见。 ', ''],
            '不辨菽麦': ['公元573年周历正月初五，晋国的栾书、中行偃派程滑杀死了晋厉公，葬在翼地的东门外边。随后，士鲂等人在京师迎按年仅14岁的周子为国君。当时，晋国的一些贵族为了自己把持朝政，很愿意事奉这位14岁的小国君，并且夸周子如何能干，如何聪明。周子有个哥哥，本应立为国君，但晋贵族们说：周子的哥哥是个白痴，连什么是豆子，什么是麦子都分不清，不能立为国君。别看这位周子才14岁，还真有些小才能。一即位，他就对大夫们说：“我开始的愿望并没有到这个地步，现在虽然到了，这全是上天的意志。人们要求有国君，是为了让他发布命令。立了以后不听他的号令，那立他干什么？你们几位用得着我才立我为君，恭敬而听从国君，这是神灵所保佑的。”大夫们听了，回答说：“这正是下臣们的愿望，岂敢不唯命是听！”“不辨菽麦”即分不清豆子和麦子。人们常用这句成语形容愚昧无知。现在有时指脱离生产实践，缺乏实际知识 ', ''],
            '不逞之徒': ['“不逞之徒”这则成语的意思是指故意为非作歹，犯法作乱，专干坏事的那一类人。不逞：不得意，欲望得不到满足。这个成语来源于《左传.襄公十年》，故五族聚群不逞之人，因公子之徒以作乱。春秋时，郑国的公子子驷，派人刺杀了郑僖公，立僖公之子嘉为国君，即郑简公。郑国一些贵族公子对此非常不满，打算发兵讨伐。可是还没动手，就被子驷察觉，抢先一步，把他们通通杀死了。从此，子驷掌握了郑国的大权。后来，子驷又重新划分贵族大夫们的封地，少给了田氏、堵氏、侯氏、子师氏四家的土地，他们都非常怨恨子驷。于是，几家就联合起五家贵族及一伙心怀不满的人，共同起来发兵讨伐子驷。最后，他们攻入国都，闯进宫中，杀死了子驷，劫持了简公。后来，子驷之子子产，平定了这次叛乱，成为郑国国君。 ', ''],
            '不耻下问': ['卫国有个大夫叫孔圉，聪敏好学，非常谦虚。孔圉后，卫国国君为了让后人学习和发扬他的好学精神，特别赐给他一个文的称号。孔子有个学生名叫子贡，也是卫国人，他认为孔圉并不像人们所说的那样好，不应得到那么高的评价。于是去问孔子：凭什么赐给孔圉‘文’的称号？孔子说：孔圉非常勤奋好学，聪明灵活，而且经常向比自己地位低下的人请教，一点儿也不感到羞耻。', ''],
            '不得要领': ['不得要领这则成语的要，即腰，指衣腰；领指衣领。古人上衣下裳，提上衣时拿着衣领，提下裳时拿着贴腰部份。要领是比喻人的意旨，这里引申为态度。现在一般来表示说话、写文章抓不住要点或关键。这个成语来源于《史记.大宛列传》，骞从月氏至大夏，竟不能得月氏要领。汉武帝初即位的时候，从北方匈奴投降过来的人都说，匈奴打败了月氏，拿月氏王的头颅骨做成大酒杯，月氏人被赶跑，对匈奴怀着强烈的仇恨。他们想攻打匈奴，但得不到别国的援助。当时，武帝正想消灭匈奴。听了这话，想和月氏友好往来。但要到月氏去，必须经过匈奴，于是招募能出使月氏的人。担任郎官不久的张骞应募出使，被武帝批准。不幸的是，张骞经过匈奴的时候，还是被抓住，押送到单于那里。单于把张骞扣留下来，并且对他说：月氏在我们的西北，你们汉人怎么能出使到那里去？如果我们要出使到越国去，你们能让我们去吗？就这样，张骞被匈奴扣留了十多年。匈奴给了他妻室，使他有了儿子，但张骞始终保存了汉朝交给他的使节。后来，匈奴放松了对张骞的监视。于是，他与随从们一起逃走，朝月氏方向前进。他们走了几十天，来到了大宛国。大宛的国王听说汉朝十分富足，想和汉朝往来，只是未能如愿；见张骞后非常高兴，问他打算到哪里去。张骞回答说：我奉汉朝之命出使去月氏，被匈奴人封锁了交通，如今从匈奴逃到这里。希望大王能派人给我带路，送我到月氏去。如果能到那里，将来回到汉朝，汉朝将赠送给你们无数财物。大宛的国王听从张骞的话，为他派出向导和翻译，一直送到了康居国，康居国又派人送他到了月氏。原来，月氏遭到匈奴人的攻击，国王被杀，大部分人西迁到了这里，称为大月氏。现在国人已立被杀国王的太子为国王，统治着早先就存在的大夏国而定居了下来。那里土地肥沃，物产丰富，没有外来的侵略，他们只想太平无事，快乐逍遥，又觉得和汉朝的距离很远，不再有向匈奴报复的心愿了。张骞从大月氏到大夏，始终不能得到月氏对与汉共击匈奴之事的明确态度。他在那里留住了一年多，就起程回国了。 ', ''],
            '不寒而栗': ['汉．司马迁《史记．酷吏列传》：汉武帝时，有个官吏叫义纵，十分凶恶残暴。他一到定襄郡上任当太守，就把狱中两百多名所谓的犯人，连同入狱探视过犯人的两百多人，全部杀害。消息传出以后，使郡中的人民都不不寒而栗。 ', ''],
            '不合时宜': ['“不合时宜”这则成语的时宜是：当时的需要。不符合时势的需要，与世情不相投合。这个成语来源于《汉书.哀帝纪》，待诏夏贺良等建言改元易号，增益漏刻，可以永安国家。朕过听贺良等言，冀为海内获福，卒亡嘉应。皆违经背古，不合时宜。汉哀帝刘欣是汉成帝的养子，二十岁即位做了皇帝，定年号为建平。自做皇帝以后，哀帝经常生病。建平二年六月，哀帝的母亲丁太后得病去世。担任“黄门待诏”的顾问官夏贺良向汉哀帝上奏说：“汉朝的历法已经衰落，应当重新接受天命。成帝当时没有顺应天命，所以他没有亲生儿子。现在，皇上您生病的时间已很长了，天下又多次发生各种变异，这些都是上天的警告。皇上只有马上改变年号，才可以延年益寿，生养皇子，平息灾祸。如果明白了这个道理而不照着做，各种灾祸都会发生，人民就要遭受灾难。”哀帝听了夏贺良的一番话，也盼自己身体健康，就在建平二年六月甲子日，即丁太后死后的第四天，发布诏书，大赦天下，改建平三年为太初元年，改帝号为“陈圣刘太平皇帝”，把计时的漏上的刻度从一百度改为一百二十度。改变年号以后，哀帝还是照样生病。夏贺良等人想趁机干预朝政，遭到朝中大臣的反对。哀帝也因夏贺良的话没有应验，派人对他们的所作所为作了调查，知道他们实际上是一伙骗子，于是在八月间又下诏书，说道：“黄门待诏夏贺良等建议改变年号和帝号，说增加漏的刻度可以使国家永远安定，我误听了他们的话，希望给天下带来安定，但是并没有应验。夏贺良等所说的所做的，都违经背古，不合时宜。六月甲子日的诏书，除了大赦一项之外，全部废除。”这次改元不到两个月就结束了。夏贺良等人因妖言惑众，被处以死刑。', ''],
            '不胫而走': ['东汉末年，孔融的好友盛孝章住在江东，虽很有才华，但却不被江东的霸主孙权所赏识。孔融便写信给曹操，向他推荐盛孝章。信中说：如果你要实现自己的政治抱负，就必须广泛招揽贤才。珠玉没有胫也会来到人们手中，这是因为人们喜爱它。而贤才是有胫的，如果你尊重他们，他们便会来投奔。孔融的建议被曹操所采纳。从此，曹操手下汇集了很多有才干的人。这个成语比喻事情不用张扬，便会迅速传播出去。 ', ''],
            '不拘一格': ['龚自珍是我国清代的思想家和文学家。1792年，他出生于浙江仁和（在今抗州）一个封建官僚家庭。他从小就喜爱读书，特别爱学写诗。14岁时，他就能写诗，18岁时会填词，20岁就成了当时著名的诗人。他写的诗，想象力很丰富，语言也瑰丽多姿，具有浪漫主义风格。他在诗中揭露了清王朝的黑暗和腐败，主张改革，支持禁烟派，反对侵略，反对妥协，充满着爱国热情。他是个爱国主义者。龚自珍27岁中举人，38岁中进士，在清朝政府里做了20年左右的官。由于他不满官场中的腐败和黑暗，一直受到排挤和打击。1839年，在他48岁时，就毅然辞官回老家。在回乡的旅途中，他看着祖国的大好河山，目睹生活在苦难中的人民，不禁触景生情，思绪万千，即兴写下了一首又一首诗。一天，龚自珍路过镇江，只见街上人山人海，热闹非凡，一打听，原来当地在赛神。人们抬着玉皇、风神、雷神等天神在虔诚地祭拜。这时，有人认出了龚自珍。一听当代文豪也在这里，一位道士马上挤上前来恳请龚自珍为天神写篇祭文。龚自珍一挥而就写下了《九州生气恃风雷》这首诗，全诗共四句：“九州生气恃风雷，万马齐喑究可哀；我劝天公重抖擞，不拘一格降人才。”诗中九州是整个中国的代称。诗的大意说，中国要有生气，要凭借疾风迅雷般的社会变革，现在人们都不敢说话，沉闷得令人可悲。我奉劝天公重新振作起来，不要拘泥于常规，把有用的人才降到人间来吧。后来，人们把“不拘一格降人才”精简成“不拘一格”这个成语，用来比喻不拘泥于一种规格、办法。诗里还引申出“万马齐喑”这个成语，比喻空气沉闷的局面。 ', ''],
            '不堪回首': ['五代南唐皇帝李煌（世称李后主）沉湎于奢侈享乐。当宋太祖赵匡胤的军队南下包围南唐都城金陵时，李煌还陶醉在歌舞声色中，结果自己也作为俘虏，被押送至开封，受到百般侮辱。一个初春的夜晚，他看到明月当空，哀秋痛苦顿时涌上心头。第二天写了首《虞美人》词，表达了他对故国及宫廷生活的怀念。其中有两句是：小楼昨夜又东风，故国不堪回首月明中。堪：可以忍受。回首：回顾.不堪回首意为回忆往事，使人痛苦难忍。 ', ''],
            '不可多得': ['东汉末年，有个名士祢衡，才华出众。当时，太中大夫孔融对他特别赏识，把他推荐给汉献帝。他写道：帝室皇居，必蓄非常之宝。若衡等辈，不可多得。汉献帝不敢作主，把孔融的荐表交给曹操。曹操爱才，就召见祢衡。哪知祢衡蔑视曹操，对他很不礼貌。曹操就派祢衡当鼓吏，在大宴宾客时，命他击鼓助兴。谁知祢衡一边击鼓，一边大骂曹操，使曹操十分难堪。曹操派祢衡去荆州劝降刘表，想借刘表之手杀他。想不到刘表把祢衡当作上宾，每次议事或发布文告，都得由祢衡表态。后来祢衡又对刘表不恭。刘表就派他到部将黄祖那里当书记。祢衡恃才傲慢，非常狂妄，后来，终于被黄祖所杀。成语不可多得由此而来，形容非常稀少、非常难得。多用于赞扬有才能的人. ', ''],
            '不可救药': ['西周的厉王，生活奢侈，骄奢淫逸，残酷地压迫和剥削人民。当时有位忠臣叫凡伯，常冒死劝谏，但厉王根本不听。那些厉王宠信的奸臣们都嘲笑凡伯。凡伯眼看着国势日衰，内心十分焦急，于是写了一首诗警告这帮人。大意如下：不是我老了，才说这些话，忧患没到来时还可防止；假若忧患越积越多，就像燃旺了的火焰，就没法救了。果然，不久以后老百姓终于忍无可忍，冲进王宫，把周厉王赶到很远的地方去了。周厉王在那儿呆了十四年，直到死去。', ''],
            '不伦不类': ['有一次，薛蟠从江南带来了两大箱东西，送给母亲薛姨妈和妹妹薛宝钗。一箱是绸缎绫罗、洋货等家常应用之物，另一箱是笔、墨、纸、砚和各种小工艺品。薛姨妈将箱子里的东西取出，一份一份地打点清楚，叫人送给贾母并王夫人等处。宝钗回到房中，将那些玩意儿一件一件过了目，除了自己留用之外，一份一份配合妥当，分送给贾府的姊妹们，就是贾环那里，她也没有忘记。林黛玉的比别人不同，而且又加厚一倍。一一打点完毕，叫人送往各处。赵姨娘见宝钗送了贾环如此东西，心里很喜欢，想道：“怪不得别人都说宝丫头好，会做人，很大方。如今看起来，果然！她哥哥能带多少东西来？她挨门送，一处也不遗漏，也不露出谁薄谁厚。连我这样没时运的，她都想到了。要是那林黛玉，她对我们娘儿正眼也不瞧，哪里还肯送我们东西？”赵姨娘一面想，一面摆弄那些东西。忽然，她又想起宝钗是王夫人的亲戚，为何不到王夫人那里去卖个好呢？于是她拿了东西走进王夫人的房中，站在旁边，陪笑说道：“这是宝姑娘才送给环哥的，难为宝姑娘这么年轻的人，想得这么周到，真是大户人家的姑娘呢，多大方，怎么不叫人敬奉呢？怪不得老太太和太太成天夸她、疼她。我也不敢自主就收起来，特地拿来给太太瞧瞧，太太也喜欢喜欢。”王夫人听了，早知道赵姨娘的来意。又见她说的话不像这类，也不像那一类，但又不便不理她，就说：“你只管收了去拿给环哥玩罢。”赵姨娘来时很高兴，谁知抹了一鼻子灰，心中生气，又不敢露出来，只得讪讪地走了. ', ''],
            '不名一钱': ['汉文帝当政的时候，有个名叫邓通的善于划船，被选到宫里当御船的水手。一天夜里，文帝做了一个梦，梦中他想升天，却怎么也上不去。就在这时候，有个头戴黄帽的人在背后推他，终于使他上了天。他回过头来看推他的人，发现那人的衣带在背后打了个结。第二天，文帝来到建在宫西苍池中的渐台，见到有个御船水手头戴黄帽,衣带在背后打了个结，正是他梦中遇见的人。召来一询问，那人名叫邓通。文帝想，他既然能把自己推上天，必定是个奇才，便非常宠爱他。邓通也老实谨慎，不随便和外人交往。文帝多次赏赐他的钱财，总数上亿之多，还授予他上大夫的官职。其实，邓通并没有什么才能。他自己处事谨慎，也不能推荐贤士，只是谄媚文帝而已。有一次，文帝命一个善于算命的人去给邓通相面，那人相面反对文帝说：“邓通这个人将来要贫饿而死。”汉文帝忧虑地说：“能让邓通富起来的只有我，我怎么会叫他受穷呢？”于是，文帝下令把蜀郡严道的一座铜山赐给邓通，允许他自已铸钱。从此邓通发了大财，他铸造的铜钱布满天下，人人都知道有“邓氏钱”。有一天，文帝背上生了个疮，脓血流个不停。邓通觉得孝顺皇帝的机会到了，便天天进宫去，用嘴巴替文帝吮吸脓血。不过，文帝心中还是不高兴。一天他问邓通：“天下谁最爱我？”邓通恭顺地回答：“应该说没有谁比太子更爱陛下的了。”一次太子刘启来看望文帝病情，文帝要他吮脓血。太子见疮口脓血模糊，腥臭难闻，禁不住一阵恶心，但又不敢违抗，只得硬着头皮吮吸，可是脸色很难看。后来他听说，邓通常为文帝吮吸脓血，感到惭愧，也因此而忌恨邓通。文帝死后，刘启即位，史称汉景帝。景帝免去邓通的官职，让他回家闲居。不久，有人告发邓通偷盗境外的铸钱。景帝派人调查，结果确有此事，便把邓通家的钱财全部没收，邓通顿时变成了穷光蛋，还欠下好几亿钱的债。还是景帝的姐姐长公主记住文帝不让他饿死的遗言，赐给他一些钱财。但是，官吏马上把这些钱财用来抵债，连一根簪子都不让他留下。长公主知道后，就让手下人借给他些衣食和钱。这样，邓通不能占有一个钱，只能寄食在别人家里直到死去。 ', ''],
            '不求甚解': ['东晋著名的文学家和诗人陶渊明，小时候家里很穷，靠很少的农田维持生计。长大后，他曾几次做官，又因为不满官场的黑暗腐败，几次辞官回家。他不贪图荣华富贵，喜欢过清静悠闲的田园生活。在耕作之余，他勤奋读书，并自称为好读书，不求甚解。意思是读书不要过于咬文嚼字，死钻牛角尖，应该深刻领会书中的要旨。这个成语比喻读书不认真，理解不深入。', ''],
            '不屈不挠': ['汉成帝建始三年秋天，长安城内流传着大水将要进城的消息。大将军王凤见城内百姓争相逃命，就劝成帝和太后及后宫嫔妃都躲到船上去。王凤还建议让官吏登上城楼避水。群臣都附和王凤的意见，只有宰相王商反对。王商认为，大水不可能一日之间突然来到，必然是谣传。不一会，长安城就安定下来。成帝派人查问，果然是谣传。成帝当众称赞了王商，批评了王凤。从此，王凤对王商怀恨在心。一次，王凤的亲家在当琅邪太守时失职，王商要惩处他。王凤主动找王商说情。王商不徇私情，还是罢免了王凤亲家的官职。王凤采取阴险手段，诬陷王商，成帝轻信王凤的话，罢免了王商的宰相职务。《汉书》作者班固评论说：王商为人朴实，性格不屈不挠，但最后还是罢官。成语不屈不挠比喻人的意志十分顽强，即使在困难或恶势力面前，也不低头、不屈服.', ''],
            '走马看花': ['唐朝中期，有位著名的诗人孟郊。他出身贫苦，从小勤奋好学，很有才华。但是，他的仕途却一直很不顺利，从青年到壮年，好几次参加进士考试都落了第。他虽然穷困潦倒，甚至连自己的家属都养不起，但他性情耿直，不肯走权贵之门。他决心刻苦攻读，用自己的真才实学，叩开仕途的大门。唐德宗贞元十三年(公元797年)，孟郊又赴京参加了一次进士考试，这次，他进士及第了，孟郊高兴极了。他穿上崭新的衣服，扎上彩带红花，骑着高头大马，在长安城里尽情地游览。京城美丽的景色使他赞叹，高中进士的喜悦又使他万分得意，于是，他写下了这首著名的《登科后》诗：昔日龌龃不足夸，今朝旷荡恩无涯；春风得意马蹄疾，一日看尽长安花。这首诗把诗人中了进士后的喜悦心情表现得淋漓尽致，其中“春风得意马蹄疾，一日看尽长安花”成为千古名句', '']
        }
        self.idiom_mean = [ # 112
            ['白手空拳', '形容手中一无所有。', ''],
            ['百般无赖', '采用所有卑鄙的方法。', ''],
            ['百川赴海', '百：表示多。川：江河。所有江河都流归大海。比喻众望所归或大势所趋。也比喻许多事物由分散而汇集到一处', ''],
            ['尺有所短', '比喻事物有其短处，并非在所有的情况下都是合适的。', ''],
            ['百川之主', '比喻事物有其短处，并非在所有的情况下都是合适的。', ''],
            ['赤贫如洗', '赤贫：穷得一无所有。形容极其贫穷。', ''],
            ['赤手光拳', '赤手：空手。两手空空，一无所有。比喻无任何凭借或一无所有。', ''],
            ['川泽纳污', '以湖泊江河能容纳各种水流的特性。比喻人有涵养，能包容所有的善恶、毁誉。', ''],
            ['垂磬之室', '磐：用石、玉制成的曲尺状打击乐器。像垂磬一样一无所有的房屋。形容十分贫困。', ''],
            ['殚财竭力', '殚、竭：尽。用尽所有的财力和人力。形容竭尽全力。', ''],
            ['凡百一新', '凡：全部；百：指事物多。所有的事物都有了新气象。', ''],
            ['分外之物', '自己名分之外的事物。指本不属于自己所有的东西，或薪俸外的收入。', ''],
            ['旮旮旯旯', '房屋、庭院、街道的所有角落及曲折隐蔽之处。', ''],
            ['盖世英雄', '盖世：压倒当世。超出当代所有的人。用以形容非常杰出的英雄人物。', ''],
            ['各行各业', '泛指所有的人所从事的各种行业。', ''],
            ['归了包堆', '所有的都包括在内，总共。', ''],
            ['环堵萧然', '环堵：围绕着四堵墙；萧然：萧条的样子。形容室中空无所有，极为贫困。', ''],
            ['黄帝子孙', '黄帝：古代传说中中华民族的共同祖先，姬姓，号轩辕氏、有熊氏。黄帝轩辕氏的子孙后代。指每个中国人或所有的中国人。', ''],
            ['浑身解数', '浑身：全身，指所有的；解数：那套数，指武艺。所有的本领，全部的权术手腕。', ''],
            ['浑俗和光', '浑俗：与世俗混同；和光：混合所有光彩。比喻不露锋芒，与世无争。也比喻无能，不中用。', ''],
            ['家道壁立', '家道：家庭经济情况；壁立：四立的墙壁。形容家贫如洗，一无所有，贫困到极点。', ''],
            ['家家户户', '每家每户。指所有的人家', ''],
            ['家徒壁立', '徒：只，仅仅。家里只有四面的墙壁。形容十分贫困，一无所有。', ''],
            ['家徒四壁', '徒：只，仅仅。家里只有四面的墙壁。形容十分贫困，一无所有。', ''],
            ['交口同声', '犹言众口一词。所有的人都说同样的话。', ''],
            ['竭忠尽智', '毫无保留地献出一片忠诚和所有才智。', ''],
            ['尽其所能', '能：能力。把所有本事都用上。', ''],
            ['尽人皆知', '尽：全部，所有。人人都知道。', ''],
            ['尽锐出战', '把所有的精锐部队派出作战。比喻派出了主力，用上了杀手锏。', ''],
            ['尽多尽少', '指尽其所有。', ''],
            ['九江八河', '泛指所有的江河。', ''],
            ['九州八极', '九州：中国古代地域共划分为九州；八极：九州之外最边远的地方。指天下所有远近的地区。', ''],
            ['居徒四壁', '徒：只，仅仅。家里只有四面的墙壁。形容十分贫困，一无所有。', ''],
            ['空空荡荡', '形容冷冷清清，空无所有的情景或指心里没着落的感觉', ''],
            ['空空洞洞', '空虚，空无所有。', ''],
            ['空空妙手', '指小偷。也形容手中一无所有。', ''],
            ['空空如也', '空空：诚恳，虚心。原形容诚恳、虚心的样子。现形容一无所有。', ''],
            ['空拳赤手', '赤手：空手。两手空空，一无所有。比喻无任何凭借或一无所有。', ''],
            ['连街倒巷', '犹言满街倾巷。指所有地方。', ''],
            ['两袖清风', '衣袖中除清风外，别无所有。比喻做官廉洁。也比喻穷得一无所有。', ''],
            ['掠人之美', '掠：夺取。夺取别人的成绩、荣誉归自己所有。', ''],
            ['妙手空空', '指小偷，也形容手中一无所有', ''],
            ['男女老少', '泛指所有的人。', ''],
            ['男女老幼', '泛指所有的人。', ''],
            ['普渡众生', '众生：指一切有生命的动物及人。佛教语。普遍引渡所有的人，使他们脱离苦海，登上彼岸。', ''],
            ['千人一状', '所有人都是一个面孔。比喻都是老一套，没有变化。', ''],
            ['倾囊相助', '囊：口袋。把衣袋里所有的钱都拿出来帮助别人。', ''],
            ['倾身营救', '比喻尽所有的力量设法去援救。', ''],
            ['倾注全力', '倾注：把精神或力量集中到一个目标。把所有力量集中在一个目标。', ''],
            ['清风两袖', '衣袖中除清风外，别无所有。比喻做官廉洁。也比喻穷得一无所有。', ''],
            ['穷山竭泽', '穷：寻求到尽头。寻遍所有的山与河。', ''],
            ['穷思毕精', '毕：尽。用尽所有的精力。', ''],
            ['人人皆知', '皆：都。所有的人都知道。', ''],
            ['扫锅刮灶', '指倾其所有。', ''],
            ['色即是空', '佛家语。指世家一切色法(物质)的本性(内在真实性)都是空无所有。', ''],
            ['身贫如洗', '穷得像死过似的，一无所有。', ''],
            ['十室九空', '室：人家。十家有九家一无所有。形容人民大量死亡或逃亡后的荒凉景象。', ''],
            ['食毛践土', '毛：指地面所生之谷物；贱：踩。原意是吃的食物和居住的土地都是国君所有。封建官吏用以表示感戴君主的恩德。', ''],
            ['世人皆知', '世人：所有人。指很多人都知道。', ''],
            ['水净鹅飞', '比喻人财两失，一无所有。亦比喻民穷财尽。', ''],
            ['通上彻下', '①指从天到地。②从上到下。指所有的人。', ''],
            ['投鞭断流', '把所有的马鞭投到江里，就能截断水流。比喻人马众多，兵力强大。', ''],
            ['万马齐喑', '喑：哑。所有的马都沉寂无声。旧时形容人民不敢讲话。现也比喻沉闷的政治局面。', ''],
            ['万能钥匙', '指能打开所有锁的钥匙。比喻解决一切困难的办法。', ''],
            ['万念俱灰', '所有的想法和打算都破灭了。形容极端灰心失望的心情。', ''],
            ['万念俱寂', '俱：全部。所有的欲望、打算都消失了。', ''],
            ['万物一府', '府：收藏财物的地方。所有的财物收藏在一起。指事物一体，无所分别。', ''],
            ['万物之情', '所有事物的情状。', ''],
            ['万象澄澈', '澄、澈：水清。万物都澄静清澈。形容月夜所有的景物澄静而清澈。', ''],
            ['小惠未遍', '惠：恩惠；遍：普遍。一点小的恩惠，不能使所有的人都得到。', ''],
            ['心心念念', '心心：指所有的心思；念念：指所有的念头。心里老是想着。指想做某件事或得到某种东西。', ''],
            ['一称心力', '一：全；称：相符合；必力：运用心思的能力。所有都跟自己所设想的心思相合。', ''],
            ['一辞同轨', '犹众口一词。所有的人都说同样的话。', ''],
            ['一家一火', '指所有家当什物。', ''],
            ['一览无遗', '览：看；遗：遗留。一眼看去，所有的景物全看见了。形容建筑物的结构没有曲折变化，或诗文内容平淡，没有回味。', ''],
            ['一览无余', '览：看；余：剩余。一眼看去，所有的景物全看见了。形容建筑物的结构没有曲折变化，或诗文内容平淡，没有回味。', ''],
            ['一切万物', '宇宙间所有的事物。', ''],
            ['英才盖世', '才：才能；盖世：压倒当世，超出世上所有的。形容超出当代、无与伦比的才能。', ''],
            ['有口皆碑', '碑：指记功碑。所有人的嘴都是活的记功碑。比喻人人称赞。', ''],
            ['占为己有', '将不是自己的东西占为自己所有。', ''],
            ['终成泡影', '结果一场空，一无所有。', ''],
            ['占为己有', '将不是自己的东西占为自己所有。', ''],
            ['众口难调', '调：协调。原意是各人的口味不同，很难做出一种饭菜使所有的人都感到好吃。比喻做事很难让所有的人都满意。', ''],
            ['众口一词', '所有的人都说同样的话。', ''],
            ['众目共睹', '所有人的眼睛都看到了。形容非常明显。亦作“众目共视”、“众目具瞻”。', ''],
            ['众目共视', '所有人的眼睛都看到了。形容非常明显。同“众目共睹”。', ''],
            ['众啄同音', '犹众口一词。所有的人都说同样的话。', ''],
            ['诸亲好友', '总称所有亲友。', ''],
            ['逐兔先得', '逐：追逐。指众人追野兔，谁先得到就归谁所有。', ''],
            ['杼柚空虚', '形容生产废弛，贫无所有。', ''],
            ['离情别绪', '分离前后惜别、相思的愁苦情绪。'],
            ['揆情度理', '按照情和理估量'],
            ['矫情镇物', '比喻故作镇静，使人无法猜度。'],
            ['径情直行', '随着意愿，顺利地得到成功。'],
            ['近乡情怯', '指远离家乡多年，不通音信，一旦返回，离家乡越近，心情越不平静，惟恐家乡发生了什么不幸的事。用以形容游子归乡时的复杂心情...'],
            ['寄兴寓情', '指作品中寄托饱含了作者的兴致与情怀。'],
            ['豪情逸致', '兴奋豪放的情感和洒脱的情趣。超逸豪放的情致。'],
            ['厚貌深情', '外貌厚道而深藏其思想感情，不流露于外表或言辞。'],
            ['含情脉脉', '是指饱含温情，默默地用眼神表达自己的感情。常用以形容少女面对意中人稍带娇羞但又无限关切的表情。'],
            ['感情用事', '凭个人的爱憎或一时的感情冲动处理事情。'],
            ['抚景伤情', '接触到面前的景物引起感情的伤痛 。'],
            ['反面无情', '形容翻脸不认人。'],
            ['反哺之情', '比喻子女长大奉养父母，报答恩情'],
            ['法不徇情', '法律不徇私情。指执法公正，不讲私人感情。'],
            ['多情善感', '感情丰富，容易伤感 。'],
            ['睹物兴情 ', '见到眼前景物便激起某种感情。'],
            ['睹景伤情', '看到景物触发起伤感之情 。'],
            ['动之以情', '用真情打动对方。'],
            ['打情骂俏', '指用轻佻的语言、动作勾引挑逗。多指男女间调情。'],
            ['捻土焚香', '因不及备香，以此表示虔诚。'],
            ['践土食毛', '指蒙受君恩；亦泛指起居生活。'],
            ['赐茅授土', '解释为封建社会帝王分封诸侯的一种礼仪。'],
            ['一览全收', '览：看。一眼看去，所有的景物全看见了。形容建筑物的结构没有曲折变化，或诗文内容平淡，没有回味。', '']
        ]
        self.idiom = [ # 1100
            '水漫金山', '重蹈覆辙', '行尸走肉', '金蝉脱壳', '百里挑一', '金玉满堂', '愚公移山', '魑魅魍魉', '背水一战', '霸王别姬',
            '天上人间', '不吐不快', '海阔天空', '情非得已', '满腹经纶', '兵临城下', '气味相投', '投鼠忌器', '屋乌之爱', '爱莫能助',
            '春暖花开', '插翅难逃', '黄道吉日', '天下无双', '偷天换日', '两小无猜', '卧虎藏龙', '珠光宝气', '簪缨世族', '花花公子',
            '绘声绘影', '国色天香', '相亲相爱', '八仙过海', '金玉良缘', '掌上明珠', '淫词艳曲', '曲终奏雅', '德高望重', '重蹈覆辙',
            '皆大欢喜', '生财有道', '极乐世界', '情不自禁', '龙生九子', '精卫填海', '海市蜃楼', '高山流水', '卧薪尝胆', '壮志凌云',
            '否极泰来', '金枝玉叶', '囊中羞涩', '霸王之资', '蠢若木鸡', '蠢头蠢脑', '清夜扪心', '心织笔耕', '离弦走板', '板上钉钉',
            '露头露脸', '巍然不动', '巍然耸立', '巍然挺立', '攀高枝儿', '蹦蹦跳跳', '翻风滚雨', '翻来复去', '翻脸无情', '翻然改悔',
            '翻手为云', '邋邋遢遢', '懵里懵懂', '懵里懵懂', '嚣浮轻巧', '鹰派人物', '耕当问奴', '奴颜婢膝', '膝痒搔背', '背信弃义',
            '胸有成竹', '竹报平安', '安富尊荣', '荣华富贵', '贵而贱目', '目无余子', '子虚乌有', '有目共睹', '睹物思人', '人中骐骥',
            '骥子龙文', '文质彬彬', '彬彬有礼', '礼贤下士', '士饱马腾', '腾云驾雾', '源源不绝', '绝甘分少', '少不经事', '美意延年',
            '雾里看花', '花言巧语', '语重心长', '长此以往', '往返徒劳', '劳而无功', '功成不居', '居官守法', '法外施仁', '仁浆义粟',
            '粟红贯朽', '朽木死灰', '灰飞烟灭', '灭绝人性', '性命交关', '关门大吉', '吉祥止止', '止于至善', '善贾而沽', '沽名钓誉',
            '象箸玉杯', '杯弓蛇影', '影影绰绰', '绰约多姿', '姿意妄为', '为人作嫁', '嫁祸于人', '人情冷暖', '暖衣饱食', '食不果腹',
            '腹背之毛', '毛手毛脚', '脚踏实地', '地老天荒', '荒诞不经', '经纬万端', '端倪可察', '察言观色', '色若死灰', '灰头土面',
            '面有菜色', '色授魂与', '面面俱到', '与民更始', '美人迟暮', '暮云春树', '树大招风', '怜香惜玉', '义无反顾', '顾全大局',
            '始乱终弃', '弃瑕录用', '用舍行藏', '藏垢纳污', '污泥浊水', '水乳交融', '融会贯通', '通宵达旦', '旦种暮成', '成人之美',
            '风中之烛', '烛照数计', '计日程功', '功德无量', '量才录用', '用行舍藏', '藏头露尾', '尾大不掉', '掉以轻心', '心急如焚',
            '焚琴煮鹤', '鹤发童颜', '颜面扫地', '地上天官', '官逼民反', '反裘负刍', '刍荛之见', '见微知著', '著作等身', '局促不安',
            '身强力壮', '壮志凌云', '云消雨散', '散兵游勇', '勇猛精进', '进退失据', '据理力争', '争长论短', '短小精悍', '悍然不顾',
            '浆酒霍肉', '肉薄骨并', '并行不悖', '悖入悖出', '出奇制胜', '胜任愉快', '快马加鞭', '鞭辟入里', '里出外进', '进寸退尺',
            '尺寸可取', '取巧图便', '便宜行事', '顾影自怜', '怜香惜玉', '玉液琼浆', '誉不绝口', '口蜜腹剑', '剑戟森森', '森罗万象',
            '事与愿违', '违心之论', '论功行赏', '赏心悦目', '目光如豆', '华而不实', '豆蔻年华', '是古非今', '今愁古恨', '恨之入骨',
            '理屈词穷', '委曲求全', '全力以赴', '穷原竟委', '赴汤蹈火', '火烧眉毛', '燎原烈火', '毛羽零落', '落井下石', '石破天惊',
            '惊惶失措', '惊惶失措', '如运诸掌', '掌上明珠', '珠沉玉碎', '碎琼乱玉', '报冰公事', '事预则立', '立身处世', '世外桃源',
            '玉碎珠沉', '沉滓泛起', '起早贪黑', '黑更半夜', '夜雨对床', '床头金尽', '尽态极妍', '妍姿艳质', '质疑问难', '难以为继',
            '继往开来', '来龙去脉', '脉脉含情', '情见势屈', '屈打成招', '招摇过市', '招摇过市', '徒劳往返', '返老还童', '童牛角马',
            '马首是瞻', '瞻前顾后', '后顾之忧', '忧国奉公', '远见卓识', '识文断字', '字斟句酌', '酌盈剂虚', '表里如一', '一呼百诺',
            '公子王孙', '孙康映雪', '雪上加霜', '霜露之病', '病病歪歪', '歪打正着', '着手成春', '春蚓秋蛇', '蛇口蜂针', '针锋相对',
            '对薄公堂', '堂堂正正', '正中下怀', '怀璧其罪', '罪大恶极', '极天际地','地丑德齐', '齐心协力', '力不胜任', '任重道远',
            '虚舟飘瓦', '瓦釜雷鸣', '鸣锣开道', '道不拾遗', '遗大投艰', '艰苦朴素', '素丝羔羊', '羊肠小道', '说长道短', '短兵相接',
            '接踵而至', '至死不变', '变本加厉', '厉行节约', '约定俗成', '成仁取义', '义形于色', '色色俱全', '全军覆灭', '灭此朝食',
            '食日万钱', '钱可通神', '神施鬼设', '设身处地', '跃跃欲试', '骨腾肉飞', '飞沿走壁', '壁垒森严', '待理不理',
            '受宠若惊', '惊涛骇浪', '浪子回头', '头疼脑热', '热火朝天', '天高地厚', '厚貌深情', '情同骨肉',
            '肉眼惠眉', '眉来眼去', '去伪存真', '真脏实犯', '犯上作乱', '乱头粗服', '分寸之末', '末学肤受',
            '服低做小', '小试锋芒', '芒刺在背', '背井离乡', '乡壁虚造', '造化小儿', '儿女情长', '长歌当哭',
            '断鹤续凫', '凫趋雀跃', '跃然纸上', '上树拔梯', '梯山航海', '海枯石烂', '烂若披锦', '锦绣前程',
            '程门立雪', '雪虐风饕', '饕餮之徒', '徒劳无功', '功败垂成', '成千上万', '哭天抹泪', '泪干肠断',
            '万象森罗', '罗雀掘鼠', '鼠窃狗盗', '盗憎主人', '人莫予毒', '毒手尊前', '前因后果', '果于自信',
            '罪恶昭彰', '彰善瘅恶', '恶贯满盈', '盈科后进', '进退两难', '难分难解', '解甲归田', '田月桑时',
            '时和年丰', '丰取刻与', '与世偃仰', '仰人鼻息', '息息相通', '通权达变', '信赏必罚', '罚不当罪',
            '变化无穷', '穷途末路', '路不拾遗', '遗臭万年', '年深日久', '久悬不决', '决一死战', '战天斗地',
            '地利人和', '和而不唱', '唱筹量沙', '沙里淘金', '金屋藏娇', '娇生惯养', '养精畜锐', '锐不可当',
            '当头棒喝', '喝西北风', '风雨同舟', '舟中敌国', '国色天香', '香火因缘', '缘木求鱼', '鱼龙混杂',
            '杂七杂八', '八拜之交', '交头接耳', '耳鬓斯磨', '磨砖成镜', '镜花水月', '月旦春秋', '秋高气爽',
            '爽然若失', '失惊打怪', '怪诞不经', '经久不息', '息事宁人', '人言啧啧', '啧有烦言', '言必有中',
            '中庸之道', '道路以目', '目瞪口呆', '呆头呆脑', '脑满肠肥', '肥马轻裘', '裘弊金尽', '尽力而为',
            '为富不仁', '仁至义尽', '尽心竭力', '力透纸背', '背道而驰', '驰名中外', '外合里差', '差强人意',
            '意在言外', '外圆内方', '方底圆盖', '盖世无双', '双管齐下', '下车伊始', '始终如一', '一蹶不振',
            '振臂一呼', '呼风唤雨', '雨沐风餐', '餐风露宿', '宿弊一清', '折槁振落', '落落大方', '方寸已乱',
            '乱琼碎玉', '玉洁冰清', '清风明月', '月盈则食', '食言而肥', '肥遁鸣高', '高朋满座', '座无虚席',
            '席卷天下', '下不为例', '例直禁简', '简明扼要', '要价还价', '价值连城', '城狐社鼠', '鼠腹鸡肠',
            '肠肥脑满', '满腔热枕', '枕石漱流', '流离转徙', '徙宅忘妻', '妻儿老小', '小本经营', '营私舞弊',
            '弊绝风清', '清尘浊水', '水磨工夫', '夫唱妇随', '随才器使', '随才器使', '使贪使愚', '愚昧无知',
            '知书达礼', '礼尚往来', '来者不拒', '来者不拒', '拒谏饰非', '非异人任', '任人唯亲', '亲密无间',
            '间不容发', '发指眦裂', '裂土分茅', '茅塞顿开', '开路先锋', '锋芒所向', '向隅而泣', '泣下如雨',
            '雨丝风片', '片言折狱', '宝山空回', '回光返照', '照本宣科', '科班出身', '身价百倍', '倍日并行',
            '行动坐卧', '卧薪尝胆', '胆破心寒', '寒木春华', '华不再扬', '扬长而去', '去粗取精', '精诚团结',
            '结党营私', '私心杂念', '念兹在兹', '兹事体大', '大势所趋', '趋炎附势', '势不两立', '立此存照',
            '照猫画虎', '虎背熊腰', '腰缠万贯', '贯朽粟陈', '陈词滥调', '调嘴学舌', '舌剑唇枪', '枪林弹雨',
            '雨过天青', '青出于蓝', '蓝田生玉', '玉卮无当', '当场出彩', '彩凤随鸦', '鸦雀无闻', '闻风而起',
            '起死回生', '生拉硬扯', '扯篷拉纤', '纤芥之疾', '纤芥之疾', '雷打不动', '动辄得咎', '咎由自取',
            '取辖投井', '井井有条''条三窝四', '四衢八街', '街头巷尾', '尾生之信', '信口开河', '河山带砺',
            '砺山带河', '河清难俟', '俟河之清', '清汤寡水', '水滴石穿', '水滴石穿', '石沉大海', '海立云垂',
            '垂涎欲滴', '滴水成冰', '冰清玉洁', '洁身自好', '好肉剜疮', '疮痍满目', '目不识丁', '丁公凿井',
            '井中视星', '星旗电戟', '戟指怒目', '目指气使', '使羊将狼', '狼心狗肺', '肺石风清',
            '安步当车', '车载斗量', '量才而为', '为渊驱鱼', '鱼游釜中', '中馈犹虚', '虚有其表',
            '诺诺连声', '声罪致讨', '讨价还价', '价增一顾', '顾盼自雄', '雄心壮志', '志美行厉',
            '厉兵秣马', '厉兵秣马', '速战速决', '决一雌雄', '雄才大略', '略见一斑', '斑驳陆离',
            '钉嘴铁舌', '舌桥不下', '下马看花', '花样翻新', '新陈代谢', '谢天谢地', '地久天长',
            '长枕大被', '被山带河', '油腔滑调', '调兵遣将', '将伯之助', '助人为乐', '乐而不淫',
            '雅俗共赏', '赏罚分明', '明刑不戮', '戮力同心', '心心相印', '印累绶若', '若有所失',
            '失张失智', '智圆行方', '方枘圆凿', '凿凿有据', '据为己有', '有眼无珠', '珠光宝气',
            '器宇轩昂', '昂首阔步', '步履维艰', '艰苦卓绝', '绝少分甘', '甘雨随车', '车水马龙',
            '龙飞凤舞', '舞衫歌扇', '扇枕温被', '被发缨冠', '冠冕堂皇', '皇天后土', '土阶茅屋',
            '助我张目', '目挑心招', '发凡起例', '事必躬亲', '亲如骨肉', '肉跳心惊', '惊弓之鸟',
            '鸟枪换炮', '龙蛇飞动', '动人心弦', '弦外之音', '音容笑貌', '貌合心离', '离心离德',
            '辙乱旗靡', '靡靡之音', '音容宛在', '在所难免', '免开尊口', '口耳之学', '学而不厌',
            '厌难折冲', '冲口而出', '出谷迁乔', '乔龙画虎', '虎踞龙盘', '盘马弯弓', '弓折刀尽', '尽善尽美',
            '年高望重', '重温旧梦', '梦寐以求', '求全之毁', '毁家纾难', '难言之隐', '隐恶扬善',
            '善始善终', '终南捷径', '径情直行', '行成于思', '思潮起伏', '伏低做小', '小恩小惠', '惠而不费', '费尽心机',
            '机关算尽', '尽忠报国', '国士无双', '双宿双飞', '飞灾横祸', '祸从天降', '降格以求',
            '求同存异', '异名同实', '实至名归', '归真反璞', '璞玉浑金', '金玉锦绣', '绣花枕头', '头没杯案', '案牍劳形',
            '舌锋如火', '火伞高张', '张冠李戴', '戴月披星', '星移斗转', '转祸为福', '福至心灵',
            '灵丹圣药', '药笼中物', '物以类聚', '聚蚊成雷', '雷厉风行', '行将就木', '木本水源', '源源不断', '断烂朝报',
            '事不师古', '兵连祸结', '结结巴巴', '巴三览四', '四面楚歌', '歌功颂德', '德厚流光', '光阴似箭', '箭在弦上',
            '上好下甚', '甚嚣尘上', '上下交困', '困知勉行', '行若无事', '事倍功半', '半夜三更',
            '更仆难数', '数见不鲜', '鲜车怒马', '马革裹尸', '尸居余气', '气冲牛斗', '斗筲之器', '盈盈一水', '水陆杂陈',
            '陈规陋习', '习焉不察', '察察为明', '明知故问', '问道于盲', '盲人摸象', '象齿焚身',
            '身不由主', '主客颠倒', '倒凤颠鸾', '鸾翔凤集', '集苑集枯', '枯木逢春', '春山如笑', '笑里藏刀', '刀山火海',
            '海外奇谈', '谈笑封侯', '侯门如海', '海阔天空', '空室清野', '野草闲花', '花颜月貌', '破颜微笑', '忘乎所以',
            '貌合神离', '离乡背井', '井蛙之见', '见仁见智', '智勇双全', '全受全归', '归马放牛', '牛骥同皂', '皂白不分',
            '分香卖履', '履舄交错', '错彩镂金', '金城汤池', '池鱼之殃', '殃及池鱼', '鱼烂而亡', '亡羊补牢', '牢不可破',
            '笑逐颜开', '开宗明义', '义薄云天', '天南地北', '北辕适楚', '楚囚对泣', '泣不成声', '声嘶力竭', '竭泽而渔',
            '渔人之利', '利令智昏', '昏天黑地', '地大物博', '博闻强识', '识途老马', '马到成功', '功德圆满', '满腹狐疑', '疑神疑鬼',
            '鬼使神差', '差三错四', '四时八节', '节衣缩食', '食而不化', '化整为零', '零打碎敲', '敲冰求火', '火树银花',
            '花好月圆', '圆颅方趾', '趾高气扬', '扬汤止沸', '沸沸扬扬', '扬幡招魂', '魂不附体', '体无完肤', '肤皮潦草', '草长莺飞',
            '飞鹰走狗', '狗吠非主', '主情造意', '意马心猿', '猿猴取月', '月露风云', '云蒸霞蔚', '蔚为大观', '观眉说眼',
            '眼馋肚饱', '饱食暖衣', '衣架饭囊', '囊空如洗', '洗耳恭听', '听而不闻', '闻鸡起舞', '舞文弄墨', '墨子泣丝', '丝恩发怨',
            '怨气冲天', '天罗地网', '网开三面', '面目全非', '非同小可', '可心如意', '意气扬扬', '扬眉吐气', '气涌如山',
            '山南海北', '北叟失马', '马仰人翻', '翻然改图', '图穷匕见', '见多识广', '广开言路', '路柳墙花', '花遮柳隐', '隐姓埋名',
            '名垂后世', '世风日下', '下车泣罪', '罪孽深重', '重于泰山', '山盟海誓', '誓死不二', '二心两意', '意气相投',
            '投机取巧', '巧取豪夺', '夺其谈经', '经年累月', '月下花前', '前思后想', '想入非非', '非亲非故', '故弄玄虚', '虚位以待',
            '待人接物', '物尽其用', '用兵如神', '神差鬼使', '使臂使指', '指不胜屈', '屈指可数', '数一数二', '二姓之好',
            '好高骛远', '远走高飞', '飞蛾投火', '火上弄冰', '冰天雪地', '地狱变相', '相机而动', '动如脱兔', '兔丝燕麦', '麦穗两歧',
            '歧路亡羊', '羊质虎皮', '皮里阳秋', '秋荼密网', '网开一面', '面红耳赤', '赤子之心', '心高气傲', '傲然屹立',
            '立功赎罪', '罪魁祸首', '首善之区', '区闻陬见', '见兔顾犬', '犬马之劳', '劳燕分飞', '火海刀山', '币重言甘', '甘棠遗爱',
            '山高水低', '低声下气', '气象万千', '千疮百孔', '孔席墨突', '突然袭击', '击节叹赏', '赏一劝百', '百年不遇',
            '遇事生风', '风雨交加', '加人一等', '等因奉此', '此起彼伏', '伏地圣人', '人欢马叫', '叫苦连天', '天高听卑', '卑礼厚币',
            '爱屋及乌', '乌焉成马', '马鹿异形', '形影相吊', '吊死问疾', '疾足先得', '得陇望蜀', '蜀犬吠日', '日升月恒',
            '恒河沙数', '数黑论黄', '黄雀伺蝉', '蝉不知雪', '雪窑冰天', '天真烂漫', '漫不经心', '心心念念', '念念不忘',
            '以指挠沸', '沸反盈天', '天上石麟', '麟趾呈祥', '祥麟威凤', '凤凰来仪', '仪静体闲', '闲云野鹤', '鹤发鸡皮',
            '皮里春秋', '秋风过耳', '耳食之谈', '谈笑自若', '谈笑自若', '若明若暗', '暗气暗恼', '恼羞成怒', '怒目而视', '视民如伤',
            '伤弓之鸟', '鸟语花香', '香花供养', '养痈成患', '患难与共', '共枝别干', '干卿底事', '事出有因', '因敌取资',
            '资深望重', '重睹天日', '日上三竿', '竿头直上', '上援下推', '推襟送抱', '抱蔓摘瓜', '绝处逢生', '多才多艺',
            '腾蛟起凤', '历历可数', '数白论黄', '黄袍加身', '身外之物', '物换星移', '移樽就教', '教学相长', '长年累月',
            '月晕而风', '风流倜傥', '傥来之物', '物是人非', '非池中物', '物极必返', '反经行权', '权宜之计', '计出万全', '全无心肝', '肝肠寸断', '深恶痛绝',
            '恕己及人', '一鞭先着', '井蛙之见', '夜宿晓行', '驰高骛远', '子承父业', '气谊相投', '划地为牢', '鹰派人物', '至高无上', '日中则移', '指挥若定',
            '一泻千里', '名闻遐迩', '暗约私期', '狗吠之警', '恨入心髓', '蝼蚁之诚', '覆公折足', '长春不老', '破觚为圆', '立吃地陷', '万赖俱寂', '指名道姓',
            '白鱼登舟', '官高爵显', '枯株朽木', '谦逊下士', '由来已久', '累教不改', '调脂弄粉', '修鳞养爪', '鹰拿燕雀', '悬圃蓬莱', '燕石妄珍', '指日可待',
            '暴虐无道', '暴虐无道', '舞词弄札', '萧敷艾荣', '奋不顾生', '如臂使指', '指不胜屈', '腹中兵甲', '指日可下', '腹背受敌', '腹热心煎', '腹热肠慌',
            '粉白黛黑', '黑白分明', '化为乌有', '有备无患', '患难之交', '交淡若水', '水过鸭背', '背城借一', '一塌糊涂', '涂脂抹粉', '明目张胆', '胆战心惊',
            '惊心悼胆', '胆大心小', '小廉曲谨', '谨毛失貌', '貌似强大', '大璞不完', '完事大吉', '吉光片羽', '羽毛未丰', '丰衣足食', '食肉寝皮', '皮相之见',
            '见笑大方', '方便之门', '门当户对', '对酒当歌', '歌舞升平', '平白无故', '从心所欲', '欲擒故纵', '大有人在', '在家出家', '吠形吠声', '接三连四',
            '故入人罪', '罪该万死', '死灰复燃', '燃眉之急', '急不暇择', '择善而从', '视同路人', '倒持泰阿', '头童齿豁', '惜墨如金', '感激涕零', '众擎易举'
        ]

    def launchRequest(self):

        """
        欢迎
        :return:
        """
        self.wait_answer()
        self.set_session_attribute("game_type", 'SkillLaunch', 0)
        bodyTemplate = BodyTemplate1()
        bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%92%B2%E5%85%AC%E8%8B%B1%E6%8A%80%E8%83%BD%E5%BC%80%E5%A7%8B%E7%95%8C%E9%9D%A2.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-22T15%3A19%3A05Z%2F-1%2F%2F037e76616226e4fb0ac9825a0b2e7b03b1b1eaa511194b49c1b64f6d298132ee')
        bodyTemplate.set_plain_text_content(r'欢迎来到蒲公英，在这里，您可以跟我一起学习英语，也可以跟我互斗成语！试着对我说，我怎么跟你玩')
        bodyTemplate.set_title('蒲公英')

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'欢迎来到蒲公英，在这里，您可以跟我一起学习英语，也可以跟我互斗成语！试着对我说，我怎么跟你玩'
        }

    def welcome(self):

        """
        介绍
        :return:
        """
        self.wait_answer()
        self.set_session_attribute("game_type", 'welcome', 0)
        bodyTemplate = BodyTemplate1()
        bodyTemplate.set_back_ground_image(
            'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%92%B2%E5%85%AC%E8%8B%B1%E6%8A%80%E8%83%BD%E5%BC%80%E5%A7%8B%E7%95%8C%E9%9D%A2.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-22T15%3A19%3A05Z%2F-1%2F%2F037e76616226e4fb0ac9825a0b2e7b03b1b1eaa511194b49c1b64f6d298132ee')
        bodyTemplate.set_plain_text_content(r'使用手册：我们这里有成语接龙、猜成语，也有英语故事、成语故事、英语笑话，还有英语歌谣和学习英语单词与短语，快来一起吧')
        bodyTemplate.set_title('蒲公英使用介绍')

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'使用手册：我们这里有成语接龙、猜成语，也有英语故事、成语故事、英语笑话，还有英语歌谣和学习英语单词与短语，快来一起吧'
        }

    def start_IdiomC(self):

        """
        成语接龙
        :return:
        """
        self.wait_answer()
        rand_id = random.randint(0, 1100)
        idiom = self.idiom
        give_idiom = idiom[rand_id]

        self.set_session_attribute("answer", give_idiom[-1], 0)
        self.set_session_attribute("give_idiom", give_idiom, 0)
        self.set_session_attribute("game_type", 'IdiomC', 0)
        self.set_session_attribute("guan_num", 1, 1)

        bodyTemplate = BodyTemplate1()
        bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E6%88%90%E8%AF%AD%E6%8E%A5%E9%BE%99.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A13%3A04Z%2F-1%2F%2F5d6ad6f2a138858a06a4f971160a007e8081249286e711d53c06410750713d71')
        bodyTemplate.set_plain_text_content(r'我先来，我出：' + give_idiom)
        bodyTemplate.set_title(r'蒲公英：成语接龙：第一关')

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'我先来，我出' + give_idiom
        }

    def tell_idiom_story(self):

        """
        成语故事
        :return:
        """
        self.wait_answer()

        result = self.get_slots('idiom_story')
        try:
            user_story = json.loads(result)
            user_story = user_story.get("origin")
        except:
            user_story = result
        if not user_story:
            self.nlu.ask('idiom_story')
        else:
            pass

        if not user_story:
            self.nlu.ask('idiom_story')
        elif user_story == 'random':

            rand_id = random.randint(0, 30)
            user_story = self.idiom_story_name[rand_id]
            idiom_story = self.idiom_story[user_story][0]

            self.set_session_attribute("idiom_story_name", user_story, 0)
            self.set_session_attribute("game_type", 'IdiomStoryRandom', 0)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E6%88%90%E8%AF%AD%E6%95%85%E4%BA%8B.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A12%3A57Z%2F-1%2F%2F3081d1933c39e44fd7195b8735caf5457a0315279125ac2406b23bdb55a99762')
            bodyTemplate.set_plain_text_content(r'好的，我们来听：' + '：' + idiom_story + '，，，还想再听一遍吗，试着对我说：再来一遍')
            bodyTemplate.set_title('蒲公英：成语故事：' + user_story)

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，我们来听：' + user_story + '，，，，' + idiom_story + '，，，还想再听一遍吗，试着对我说，再来一遍'
            }
        else:
            try:
                idiom_story = self.idiom_story[user_story][0]
            except KeyError:
                return {
                    'outputSpeech': r'真是对不起了，我这里没有这个成语故事'
                }
            else:
                pass
            self.set_session_attribute("idiom_story_name", user_story, 0)
            self.set_session_attribute("game_type", 'IdiomStoryNormal', 0)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E6%88%90%E8%AF%AD%E6%95%85%E4%BA%8B.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A12%3A57Z%2F-1%2F%2F3081d1933c39e44fd7195b8735caf5457a0315279125ac2406b23bdb55a99762')
            bodyTemplate.set_plain_text_content(r'好的，我们来听：' + user_story +  '：' + idiom_story + '还想再听一遍吗，试着对我说：再来一遍')
            bodyTemplate.set_title(user_story)

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，我们来听：' + user_story +  '，，，，' + idiom_story + '还想再听一遍吗，试着对我说，再来一遍'
            }

    def start_IdiomGuess(self):

        """
        猜成语
        :return:
        """
        self.wait_answer()
        result = self.get_slots('guess_mode')
        try:
            mode = json.loads(result)
            mode = mode.get("origin")
        except:
            mode = result
        if not mode:
            self.nlu.ask('guess_mode')
        else:
            pass

        if mode == 'blank':

            rand_id = random.randint(0, 1100)
            rand_ids = random.randint(0, 3)
            answer = self.idiom[rand_id]
            give_idiom = answer.replace(answer[rand_ids] + answer[rand_ids + 1], '*')
            self.set_session_attribute("real_answer", answer, 0)
            self.set_session_attribute("give_idiom", give_idiom, '')
            self.set_session_attribute("game_type", 'IdiomGuessBlank', 0)
            self.set_session_attribute("guan_num", 1, 1)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%8C%9C%E6%88%90%E8%AF%AD.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A21%3A37Z%2F-1%2F%2F05ab264f18c6ae80d701ea2245435acc0817a67d35e0d8d6522535208ae0e73d')
            bodyTemplate.set_plain_text_content(r'诶呀！我吃掉了成语的一部分，快来帮我还原吧!   ' + give_idiom)
            bodyTemplate.set_title(r'蒲公英：填空猜成语：第一关')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'诶呀！我吃掉了成语的一部分，快来帮我还原吧!   ' + give_idiom
            }
        elif mode == 'means':

            rand_id = random.randint(0, 89)
            ask = self.idiom_mean[rand_id][1]
            self.set_session_attribute("real_answer", self.idiom_mean[rand_id][0], 0)
            self.set_session_attribute("idiom_means_num", rand_id, 0)
            self.set_session_attribute("game_type", 'IdiomGuessMeans', 0)
            self.set_session_attribute("guan_num", 1, 1)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%8C%9C%E6%88%90%E8%AF%AD.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A21%3A37Z%2F-1%2F%2F05ab264f18c6ae80d701ea2245435acc0817a67d35e0d8d6522535208ae0e73d')
            bodyTemplate.set_plain_text_content(r'好啊，这个是哪个成语的意思呢：' + ask)
            bodyTemplate.set_title(r'蒲公英：意思猜成语：第一关')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好啊，这个是哪个成语的意思呢，，，，' + ask
            }
        elif not mode:
            self.nlu.ask('guess_mode')

    def tell_english_story(self):

        """
        英语故事
        :return:
        """
        self.set_session_attribute("game_type", 'EnglishStory', 0)
        rand_id = random.randint(0, 65)
        story = self.english_story[rand_id]
        self.set_session_attribute("english_story_num", rand_id, 0)

        bodyTemplate = BodyTemplate1()
        bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%8B%B1%E8%AF%AD%E6%95%85%E4%BA%8B.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A13%3A22Z%2F-1%2F%2F58ec0c03668d27d86a3aff6611185a2aae02def659de4b420f64651deed1b01b')
        bodyTemplate.set_plain_text_content(r'好啊，让我们一起来看英语故事吧！' + story + '。好看吗？要再来一个吗？试着对我说“再来一个”')
        bodyTemplate.set_title(r'蒲公英：英语故事')

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'好啊，让我们一起来看英语故事吧，，，' + story
        }

    def tell_english_joke(self):

        """
        英语笑话
        :return:
        """
        self.set_session_attribute("game_type", 'EnglishJoke', 0)
        rand_id = random.randint(0, 65)
        joke = self.english_joke[rand_id][0]
        self.set_session_attribute("english_joke_num", rand_id, 0)

        bodyTemplate = BodyTemplate1()
        bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%8B%B1%E8%AF%AD%E7%AC%91%E8%AF%9D.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A13%3A08Z%2F-1%2F%2F276b3ab30535bca9d0aa1fdded1fdc0fc2f441ebc7cc1d656e64bb74f423dfe2')
        bodyTemplate.set_plain_text_content(r'好啊，让我们来搞笑一下吧！' + joke + '。好笑吗？试着对我说“再来一个”')
        bodyTemplate.set_title(r'蒲公英：英语笑话')

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'好啊，让我们来搞笑一下吧，，，' + joke
        }


    def study_english_word(self):

        """
        学习英语单词
        :return:
        """
        self.set_session_attribute("game_type", 'EnglishWord', 0)
        rand_id = random.randint(0, 123)
        self.set_session_attribute("english_word_num", rand_id, 0)

        bodyTemplate = BodyTemplate1()
        bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%8B%B1%E8%AF%AD%E5%8D%95%E8%AF%8D.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A13%3A07Z%2F-1%2F%2F4e733c54b0712327c033cd46ff93ef0e6276d9691216419841c3f09f7578e5a8')
        bodyTemplate.set_plain_text_content(r'这个是' + self.english_word[rand_id][0])
        bodyTemplate.set_title(r'蒲公英：英语单词：' + self.english_word[rand_id][0] + '，再来一个呗，试着对我说“下一个”')

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'这个是' + self.english_word[rand_id][0] + '，再来一个呗，试着对我说“下一个”'
        }



    def english_song(self):

        """
        英语歌曲
        :return:
        """
        self.set_session_attribute("game_type", 'EnglishSong', 0)
        rand_id = random.randint(0, 65)
        self.set_session_attribute("english_song_num", rand_id, 0)

        directives = []
        directive = Play(self.english_song[rand_id][0], PlayBehaviorEnum.REPLACE_ALL)
        directives.append(directive)
        return {
            'directives': directives,
            'outputSpeech': '好啊，让我们来听一下英语歌曲吧',
        }

    def more_one(self):

        """
        再来一个
        :return:
        """
        self.wait_answer()
        game_type = self.get_session_attribute("game_type", 0)
        if game_type == 'EnglishSong':

            rand_id = random.randint(0, 65)

            while 1 == 1:
                if self.get_session_attribute("english_song_num", 0) == rand_id:
                    rand_id = random.randint(0, 65)
                else:
                    break

            self.set_session_attribute("english_song_num", rand_id, 0)
            self.set_session_attribute("game_type", 'EnglishSong', 0)

            directives = []
            directive = Play(self.english_song[rand_id][0], PlayBehaviorEnum.REPLACE_ALL)
            directives.append(directive)
            return {
                'directives': directives,
                'outputSpeech': '好的，再来一首英语歌谣',
            }
        elif game_type == 'EnglishWord':


            rand_id = random.randint(0, 123)

            while 1 == 1:
                if self.get_session_attribute("english_song_num", 0) == rand_id:
                    rand_id = random.randint(0, 65)
                else:
                    break

            self.set_session_attribute("game_type", 'EnglishWord', 0)
            self.set_session_attribute("english_word_num", rand_id, 0)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%8B%B1%E8%AF%AD%E5%8D%95%E8%AF%8D.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A13%3A07Z%2F-1%2F%2F4e733c54b0712327c033cd46ff93ef0e6276d9691216419841c3f09f7578e5a8')
            bodyTemplate.set_plain_text_content(r'这个是' + self.english_word[rand_id][0])
            bodyTemplate.set_title(r'蒲公英：英语单词：' + self.english_word[rand_id][0])

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'你好学的精神感动了我，再来一个！这个是' + self.english_word[rand_id][0]
            }
        elif game_type == 'EnglishJoke':


            rand_id = random.randint(0, 65)

            while 1 == 1:
                if self.get_session_attribute("english_song_num", 0) == rand_id:
                    rand_id = random.randint(0, 65)
                else:
                    break

            joke = self.english_joke[rand_id][0]

            self.set_session_attribute("game_type", 'EnglishJoke', 0)
            self.set_session_attribute("english_joke_num", rand_id, 0)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%8B%B1%E8%AF%AD%E6%95%85%E4%BA%8B.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A13%3A22Z%2F-1%2F%2F58ec0c03668d27d86a3aff6611185a2aae02def659de4b420f64651deed1b01b')
            bodyTemplate.set_plain_text_content(r'好的，笑一笑更健康！让我们再来一个' + joke)
            bodyTemplate.set_title(r'蒲公英：英语笑话')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，笑一笑更健康！让我们再来一个' + joke
            }
        elif game_type == 'EnglishStory':


            rand_id = random.randint(0, 65)

            while 1 == 1:
                if self.get_session_attribute("english_song_num", 0) == rand_id:
                    rand_id = random.randint(0, 65)
                else:
                    break

            story = self.english_story[rand_id]

            self.set_session_attribute("english_story_num", rand_id, 0)
            self.set_session_attribute("game_type", 'EnglishStory', 0)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%8B%B1%E8%AF%AD%E6%95%85%E4%BA%8B.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A13%3A22Z%2F-1%2F%2F58ec0c03668d27d86a3aff6611185a2aae02def659de4b420f64651deed1b01b')
            bodyTemplate.set_plain_text_content(r'好的，英语故事等着您呢！' + story)
            bodyTemplate.set_title(r'蒲公英：英语故事')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，英语故事等着您呢！' + story
            }
        elif game_type == 'IdiomStoryRandom' or game_type == 'IdiomStoryNormal':

            rand_id = random.randint(0, 65)
            user_story = self.idiom_story_name[rand_id]
            idiom_story = self.idiom_story[user_story][0]

            self.set_session_attribute("idiom_story_name", user_story, 0)
            self.set_session_attribute("game_type", 'IdiomStoryRandom', 0)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image(
                'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E6%88%90%E8%AF%AD%E6%95%85%E4%BA%8B.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A12%3A57Z%2F-1%2F%2F3081d1933c39e44fd7195b8735caf5457a0315279125ac2406b23bdb55a99762')
            bodyTemplate.set_plain_text_content(r'好的，再来一个' + '：' + idiom_story)
            bodyTemplate.set_title('蒲公英：成语故事：' + user_story)

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，再来一个：' + user_story + '，，，，' + idiom_story
            }
        else:
            return {
                'outputSpeech': r'对不起，我不知道您要再来什么'
            }

    def next_one(self):

        """
        下一个
        :return:
        """
        self.wait_answer()
        game_type = self.get_session_attribute("game_type", 0)
        if game_type == 'IdiomGuessMeans':

            guan = self.get_session_attribute("guan_num", 0)
            rand_id = random.randint(0, 89)
            ask = self.idiom_mean[rand_id][1]
            self.set_session_attribute("real_answer", self.idiom_mean[rand_id][0], 0)
            self.set_session_attribute("idiom_means_num", rand_id, 0)
            self.set_session_attribute("game_type", 'IdiomGuessMeans', 0)
            self.set_session_attribute("guan_num", guan + 1, 1)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%8C%9C%E6%88%90%E8%AF%AD.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A21%3A37Z%2F-1%2F%2F05ab264f18c6ae80d701ea2245435acc0817a67d35e0d8d6522535208ae0e73d')
            bodyTemplate.set_plain_text_content(r'好的，让我们进入第' + guan + '关，那么这个意思是哪个成语呢：' + ask)
            bodyTemplate.set_title(r'蒲公英：填空猜成语：第' + str(guan + 1) + '关')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，让我们进入第' + str(guan + 1) + '关，那么这个意思是哪个成语呢：' + ask
            }

        elif game_type == 'IdiomGuessBlank':

            guan = self.get_session_attribute("guan_num", 0)
            rand_id = random.randint(0, 1100)
            rand_ids = random.randint(0, 3)
            answer = self.idiom[rand_id]
            give_idiom = answer.replace(answer[rand_ids] + answer[rand_ids + 1], '*')
            self.set_session_attribute("real_answer", answer, 0)
            self.set_session_attribute("give_idiom", give_idiom, '')
            self.set_session_attribute("game_type", 'IdiomGuessBlank', 0)
            self.set_session_attribute("guan_num", guan + 1, 1)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image(
                'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%8C%9C%E6%88%90%E8%AF%AD.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A21%3A37Z%2F-1%2F%2F05ab264f18c6ae80d701ea2245435acc0817a67d35e0d8d6522535208ae0e73d')
            bodyTemplate.set_plain_text_content(r'诶呀！我吃掉了成语的一部分，快来帮我还原吧!   ' + give_idiom)
            bodyTemplate.set_title(r'蒲公英：意思猜成语：第' + str(guan + 1) + '关')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'诶呀！我吃掉了成语的一部分，快来帮我还原吧!   ' + give_idiom
            }

        elif game_type == 'IdiomC':

            rand_id = random.randint(0, 1100)
            idiom = self.idiom
            give_idiom = idiom[rand_id]

            self.set_session_attribute("answer", give_idiom[-1], 0)
            self.set_session_attribute("give_idiom", give_idiom, 0)
            self.set_session_attribute("game_type", 'IdiomC', 0)
            self.set_session_attribute("guan_num", self.get_session_attribute("guan_num", 0) + 1, 1)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image(
                'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E6%88%90%E8%AF%AD%E6%8E%A5%E9%BE%99.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A13%3A04Z%2F-1%2F%2F5d6ad6f2a138858a06a4f971160a007e8081249286e711d53c06410750713d71')
            bodyTemplate.set_plain_text_content(r'好的，让我们进入下一关，我先来，我出' + give_idiom)
            bodyTemplate.set_title(r'蒲公英：成语接龙：第' + str(self.get_session_attribute("guan_num", 1)) + '关')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，让我们进入下一关，我先来，我出' + give_idiom
            }





    def answer_helper(self):

        """
        提示
        :return:
        """
        self.wait_answer()
        game_type = self.get_session_attribute("game_type", 0)
        if game_type == 'IdiomC':

            answer = self.get_session_attribute("answer", 0)
            give_idiom = self.get_session_attribute("give_idiom", 0)
            a = 0
            helper_idiom = ''
            idiom = self.idiom
            while 1 == 1:
                try:
                    test = idiom[a]
                except IndexError:
                    break
                else:
                    if idiom[a][0] == answer:
                        helper_idiom = idiom[a][0] + idiom[a][1]
                        if helper_idiom == give_idiom:
                            a = a + 1
                        else:
                            break
                    else:
                        a = a + 1

            if helper_idiom == '' or helper_idiom == None:

                bodyTemplate = BodyTemplate1()
                bodyTemplate.set_back_ground_image(
                    'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%92%B2%E5%85%AC%E8%8B%B1%E6%8A%80%E8%83%BD%E6%8F%90%E7%A4%BA%E8%83%8C%E6%99%AF%E5%9B%BE.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-24T13%3A11%3A07Z%2F-1%2F%2F4ba21633f203946933f383d470b953e554cb6ff25be338d59b3379f7ffe68e46')
                bodyTemplate.set_plain_text_content(r'诶呀，提示不见了，努力想想吧')

                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': r'诶呀，提示不见了，努力想想吧'
                }

            else:

                bodyTemplate = BodyTemplate1()
                bodyTemplate.set_back_ground_image(
                    'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%92%B2%E5%85%AC%E8%8B%B1%E6%8A%80%E8%83%BD%E6%8F%90%E7%A4%BA%E8%83%8C%E6%99%AF%E5%9B%BE.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-24T13%3A11%3A07Z%2F-1%2F%2F4ba21633f203946933f383d470b953e554cb6ff25be338d59b3379f7ffe68e46')
                bodyTemplate.set_plain_text_content(r'给你前两个字，想想,' + helper_idiom + '**如果实在想不到，可以对我说，跳过，')

                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': r'给你前两个字，想想,' + helper_idiom + '，，，如果实在想不到，可以对我说，跳过，'
                }
        elif game_type == 'IdiomGuessBlank':

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image(
                'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%92%B2%E5%85%AC%E8%8B%B1%E6%8A%80%E8%83%BD%E6%8F%90%E7%A4%BA%E8%83%8C%E6%99%AF%E5%9B%BE.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-24T13%3A11%3A07Z%2F-1%2F%2F4ba21633f203946933f383d470b953e554cb6ff25be338d59b3379f7ffe68e46')
            bodyTemplate.set_plain_text_content(r'这个那么简单，不用提示了吧')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'这个那么简单，不用提示了吧'
            }
        elif game_type == 'IdiomGuessMeans':

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image(
                'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E8%92%B2%E5%85%AC%E8%8B%B1%E6%8A%80%E8%83%BD%E6%8F%90%E7%A4%BA%E8%83%8C%E6%99%AF%E5%9B%BE.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-24T13%3A11%3A07Z%2F-1%2F%2F4ba21633f203946933f383d470b953e554cb6ff25be338d59b3379f7ffe68e46')
            bodyTemplate.set_plain_text_content(r'给你前两个字，想一想，' + self.get_session_attribute("real_answer", 0)[0] + self.get_session_attribute("real_answer", 0)[1])

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'给你前两个字，想一想，' + self.get_session_attribute("real_answer", 0)[0] + self.get_session_attribute("real_answer", 0)[1]
            }
        else:
            return {
                'outputSpeech': r'对不起，我不知道您要什么提示'
            }


    def c_game(self):

        """
        继续游戏
        :return:
        """
        self.wait_answer()
        game_type = self.get_session_attribute("game_type", 0)
        if game_type == 'IdiomC':
            give_idiom = self.get_session_attribute("give_idiom", '')
            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image(
                'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E6%88%90%E8%AF%AD%E6%8E%A5%E9%BE%99.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A13%3A04Z%2F-1%2F%2F5d6ad6f2a138858a06a4f971160a007e8081249286e711d53c06410750713d71')
            bodyTemplate.set_plain_text_content(r'好的，我们继续，我刚刚出了：' + give_idiom)

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，我们继续，我刚刚出了' + give_idiom
            }
        elif game_type == 'IdiomGuessBlank':

            give_idiom = self.get_session_attribute("give_idiom", 0)
            guan = self.get_session_attribute("guan_num", 1)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image(
                'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%8C%9C%E6%88%90%E8%AF%AD.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A21%3A37Z%2F-1%2F%2F05ab264f18c6ae80d701ea2245435acc0817a67d35e0d8d6522535208ae0e73d')
            bodyTemplate.set_plain_text_content(r'好的，我们继续填空猜成语：' + give_idiom)
            bodyTemplate.set_title(r'蒲公英：填空猜成语：第' + str(guan) + '关')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，我们继续填空猜成语：' + give_idiom
            }
        elif game_type == 'IdiomGuessMeans':

            ask = self.idiom_mean[self.get_session_attribute("idiom_mean_num", 0)][1]
            guan = self.get_session_attribute("guan_num", 1)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.set_back_ground_image(
                'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%8C%9C%E6%88%90%E8%AF%AD.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A21%3A37Z%2F-1%2F%2F05ab264f18c6ae80d701ea2245435acc0817a67d35e0d8d6522535208ae0e73d')
            bodyTemplate.set_plain_text_content(r'好的，让我们继续意思猜成语' + ask )
            bodyTemplate.set_title(r'蒲公英：意思猜成语：第' + str(guan) + '关')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，让我们继续意思猜成语' + ask
            }
        else:
            return {
                'outputSpeech': r'对不起，我不知道您要继续什么游戏'
            }

    def answer(self):

        """
        回答
        :return:
        """
        self.wait_answer()

        game_type = self.get_session_attribute("game_type", 0)

        result = self.get_slots('idiom')
        try:
            user_answer = json.loads(result)
            user_answer = user_answer.get("origin")
        except:
            user_answer = result
        if not user_answer:
            self.nlu.ask('idiom')
        else:
            pass


        if game_type == 'IdiomC': # 成语接龙正确错误判断


            a = 0
            real_answer = self.get_session_attribute("give_idiom", 0)
            answer = self.get_session_attribute("answer", 0)
            guan = self.get_session_attribute("guan_num", 0)
            if user_answer[0] != real_answer[3]:
                # 错误分支

                idiom = self.idiom
                while 1 == 1:
                    try:
                        test = idiom[a]
                    except IndexError:
                        break
                    else:
                        if idiom[a][0] == real_answer[-1]:
                            new_give_idiom = idiom[a]
                            if new_give_idiom == user_answer:
                                a = a + 1
                            else:
                                break
                        else:
                            a = a + 1
                if not new_give_idiom:
                    new_give_idiom = '。。。诶呀！突然发现我也接不了，我们重新来吧，对我说“重新开始”'
                else:
                    pass
                self.set_session_attribute("answer", new_give_idiom[-1], '')
                self.set_session_attribute("give_idiom", new_give_idiom, '')
                self.set_session_attribute("guan_num", self.get_session_attribute("guan_num", 1) + 1, 1)

                bodyTemplate = BodyTemplate1()
                bodyTemplate.set_back_ground_image('http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%AD%94%E9%94%99%E4%BA%86.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A12%3A59Z%2F-1%2F%2F93d5f20ef7979ef40c3da594888b5227c14e5740eb9c31cc7ac29e1334194680')
                bodyTemplate.set_plain_text_content(r'接错了哦，你可以接' + new_give_idiom + '，好的，接下来我出' + new_give_idiom)
                bodyTemplate.set_title('蒲公英：成语接龙：第' + str(guan) + '关')

                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': r'接错了哦，你可以接' + new_give_idiom + '，好的，接下来我出' + new_give_idiom
                }

            else:

                # 正确分支
                idiom = self.idiom
                while 1 == 1:
                        try:
                            test = idiom[a]
                        except IndexError:
                            break
                        else:
                            if idiom[a][0] == user_answer[-1]:
                                new_give_idiom = idiom[a]
                                if new_give_idiom == real_answer:
                                    a = a + 1
                                else:
                                    break
                            else:
                                a = a + 1
                if not new_give_idiom:
                    return {
                        'outputSpeech': '诶呀，你这下真的打败我了，我输了，对我说，重新开始成语接龙，'
                    }
                else:
                    self.set_session_attribute("answer", new_give_idiom[-1], '')
                    self.set_session_attribute("give_idiom", new_give_idiom, '')
                    self.set_session_attribute("guan_num", self.get_session_attribute("guan_num", 1) + 1, 1)

                    bodyTemplate = BodyTemplate1()
                    bodyTemplate.set_back_ground_image(
                        'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%AD%94%E5%AF%B9.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A13%3A21Z%2F-1%2F%2Fd2f43299bddab52cfb966a8115303b8a18e934e8cb5b7b34ec0c4b376a72c513')
                    bodyTemplate.set_plain_text_content(r'你真棒，被你接到了，那么我接' + new_give_idiom)
                    bodyTemplate.set_title('蒲公英：成语接龙：第' + str(guan) + '关')

                    directive = RenderTemplate(bodyTemplate)
                    return {
                        'directives': [directive],
                        'outputSpeech': r'你真棒，被你接到了，那么我接' + new_give_idiom
                    }
        elif game_type == 'IdiomGuessBlank': # 填空猜成语正确错误判断

            # 正确分支
            real_answer = self.get_session_attribute("real_answer", 0)
            if user_answer == real_answer:

                bodyTemplate = BodyTemplate1()
                bodyTemplate.set_back_ground_image(
                    'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%8C%9C%E6%88%90%E8%AF%AD.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A21%3A37Z%2F-1%2F%2F05ab264f18c6ae80d701ea2245435acc0817a67d35e0d8d6522535208ae0e73d')
                bodyTemplate.set_plain_text_content(r'恭喜你，答对了，要继续，请对我说“下一关”')
                bodyTemplate.set_title('答对了')

                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': r'恭喜你，答对了，要继续，请对我说“下一关”'
                }

            else:

                # 错误分支
                bodyTemplate = BodyTemplate1()
                bodyTemplate.set_back_ground_image(
                    'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%8C%9C%E6%88%90%E8%AF%AD.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A21%3A37Z%2F-1%2F%2F05ab264f18c6ae80d701ea2245435acc0817a67d35e0d8d6522535208ae0e73d')
                bodyTemplate.set_plain_text_content(r'好遗憾，答错了，正确答案是' + real_answer + '，你可以对我说“下一关”即可进入下一关')
                bodyTemplate.set_title('答错了')

                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': r'好遗憾，答错了，正确答案是' + real_answer + '，你可以对我说“下一关”即可进入下一关'
                }
        elif game_type == 'IdiomGuessMeans':

            real_answer = self.get_session_attribute("real_answer", 0)
            if user_answer == real_answer:

                bodyTemplate = BodyTemplate1()
                bodyTemplate.set_back_ground_image(
                    'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%8C%9C%E6%88%90%E8%AF%AD.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A21%3A37Z%2F-1%2F%2F05ab264f18c6ae80d701ea2245435acc0817a67d35e0d8d6522535208ae0e73d')
                bodyTemplate.set_plain_text_content(r'恭喜你！答对了！对我说“下一关”即可进入下一关')
                bodyTemplate.set_title('答对了')

                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': r'恭喜你！答对了！对我说“下一关”即可进入下一关'
                }
            else:

                bodyTemplate = BodyTemplate1()
                bodyTemplate.set_back_ground_image(
                    'http://dbp-resource.gz.bcebos.com/d794e4f2-b2d5-4302-c42d-f34781a54abf/%E7%8C%9C%E6%88%90%E8%AF%AD.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-23T13%3A21%3A37Z%2F-1%2F%2F05ab264f18c6ae80d701ea2245435acc0817a67d35e0d8d6522535208ae0e73d')
                bodyTemplate.set_plain_text_content(r'好遗憾，答错了，你可以回答' + real_answer + '，你可以对我说“下一关”即可进入下一关')
                bodyTemplate.set_title('答错了')

                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': r'好遗憾，答错了，你可以回答' + real_answer + '，你可以对我说“下一关”即可进入下一关'
                }

    def quesheng(self):
        
            """
            缺省
            :return:
            """
            self.wait_answer()
            try:
                text = self.data['request']['query']['original']
            except:
                return {
                    'outputSpeech': r'答错了哦！需要帮助可以对我说，我需要帮助'
                }
            else:
                if len(text) == 4:
                    return {
                        'outputSpeech': r'答错了哦！需要帮助可以对我说，我需要帮助'
                    }
                else:
                    return {
                        'outputSpeech': r'您说的我没有理解，对不起，您可以对我说，使用手册'
                    }
