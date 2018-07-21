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

class IdiomMaster(Bot):

    def __init__(self, data):

        super().__init__(data)
        self.data = data
        self.addLaunchHandler(self.launchRequest)
        self.addIntentHandler('start_IdiomC', self.start_IdiomC)
        self.addIntentHandler('start_IdiomStory', self.start_IdiomStory)
        self.addIntentHandler('start_IdiomGuess', self.start_IdiomGuess)
        self.addIntentHandler('answer', self.answer)
        self.addIntentHandler('round', self.round)
        self.addIntentHandler('answer_helper', self.answer_helper)
        self.addIntentHandler('c_game', self.quesheng)
        self.addIntentHandler('ai.dueros.common.default_intent', self.quesheng)
        self.idiom = [
            '水漫金山', '重蹈覆辙', '行尸走肉', '金蝉脱壳', '百里挑一', '金玉满堂', '愚公移山', '魑魅魍魉', '背水一战', '霸王别姬',
            '天上人间', '不吐不快', '海阔天空', '情非得已', '满腹经纶', '兵临城下',
            '春暖花开', '插翅难逃', '黄道吉日', '天下无双', '偷天换日', '两小无猜', '卧虎藏龙', '珠光宝气', '簪缨世族', '花花公子',
            '绘声绘影', '国色天香', '相亲相爱', '八仙过海', '金玉良缘', '掌上明珠',
            '皆大欢喜', '生财有道', '极乐世界', '情不自禁', '龙生九子', '精卫填海', '海市蜃楼', '高山流水', '卧薪尝胆', '壮志凌云',
            '否极泰来', '金枝玉叶', '囊中羞涩', '霸王之资', '蠢若木鸡', '蠢头蠢脑',
            '露头露脸', '巍然不动', '巍然耸立', '巍然挺立', '攀高枝儿', '蹦蹦跳跳', '翻风滚雨', '翻来复去', '翻脸无情', '翻然改悔',
            '翻手为云', '邋邋遢遢', '懵里懵懂', '懵里懵懂', '嚣浮轻巧', '鹰派人物',
            '胸有成竹', '竹报平安', '安富尊荣', '荣华富贵', '贵而贱目', '目无余子', '子虚乌有', '有目共睹', '睹物思人', '人中骐骥',
            '骥子龙文', '文质彬彬', '彬彬有礼', '礼贤下士', '士饱马腾', '腾云驾雾',
            '雾里看花', '花言巧语', '语重心长', '长此以往', '往返徒劳', '劳而无功', '功成不居', '居官守法', '法外施仁', '仁浆义粟',
            '粟红贯朽', '朽木死灰', '灰飞烟灭', '灭绝人性', '性命交关', '关门大吉', '吉祥止止', '止于至善', '善贾而沽', '沽名钓誉', '誉不绝口', '口蜜腹剑', '剑戟森森', '森罗万象',
            '象箸玉杯', '杯弓蛇影', '影影绰绰', '绰约多姿', '姿意妄为', '为人作嫁', '嫁祸于人', '人情冷暖', '暖衣饱食', '食不果腹',
            '腹背之毛', '毛手毛脚', '脚踏实地', '地老天荒', '荒诞不经', '经纬万端', '端倪可察', '察言观色', '色若死灰', '灰头土面', '面有菜色', '色授魂与', '面面俱到', '与民更始',
            '始乱终弃', '弃瑕录用', '用舍行藏', '藏垢纳污', '污泥浊水', '水乳交融', '融会贯通', '通宵达旦', '旦种暮成', '成人之美',
            '美人迟暮', '暮云春树', '树大招风', '怜香惜玉',
            '风中之烛', '烛照数计', '计日程功', '功德无量', '量才录用', '用行舍藏', '藏头露尾', '尾大不掉', '掉以轻心', '心急如焚',
            '焚琴煮鹤', '鹤发童颜', '颜面扫地', '地上天官', '官逼民反', '反裘负刍', '刍荛之见', '见微知著', '著作等身',
            '身强力壮', '壮志凌云', '云消雨散', '散兵游勇', '勇猛精进', '进退失据', '据理力争', '争长论短', '短小精悍', '悍然不顾',
            '顾影自怜', '怜香惜玉', '玉液琼浆',
            '浆酒霍肉', '肉薄骨并', '并行不悖', '悖入悖出', '出奇制胜', '胜任愉快', '快马加鞭', '鞭辟入里', '里出外进', '进寸退尺',
            '尺寸可取', '取巧图便', '便宜行事',
            '事与愿违', '违心之论', '论功行赏', '赏心悦目', '目光如豆', '华而不实', '豆蔻年华', '是古非今', '今愁古恨', '恨之入骨',
            '骨腾肉飞', '飞沿走壁', '壁垒森严', '待理不理',
            '理屈词穷', '委曲求全', '全力以赴', '穷原竟委', '赴汤蹈火', '火烧眉毛', '燎原烈火', '毛羽零落', '落井下石', '石破天惊',
            '惊惶失措', '惊惶失措', '如运诸掌', '掌上明珠', '珠沉玉碎', '碎琼乱玉',
            '玉碎珠沉', '沉滓泛起', '起早贪黑', '黑更半夜', '夜雨对床', '床头金尽', '尽态极妍', '妍姿艳质', '质疑问难', '难以为继',
            '继往开来', '来龙去脉', '脉脉含情', '情见势屈', '屈打成招', '招摇过市', '招摇过市', '徒劳往返', '返老还童', '童牛角马',
            '马首是瞻', '瞻前顾后', '后顾之忧', '忧国奉公',
            '公子王孙', '孙康映雪', '雪上加霜', '霜露之病', '病病歪歪', '歪打正着', '着手成春', '春蚓秋蛇', '蛇口蜂针', '针锋相对',
            '对薄公堂', '堂堂正正', '正中下怀', '怀璧其罪', '罪大恶极', '极天际地','地丑德齐', '齐心协力', '力不胜任', '任重道远',
            '远见卓识', '识文断字', '字斟句酌', '酌盈剂虚',
            '虚舟飘瓦', '瓦釜雷鸣', '鸣锣开道', '道不拾遗', '遗大投艰', '艰苦朴素', '素丝羔羊', '羊肠小道', '说长道短', '短兵相接',
            '接踵而至', '至死不变', '变本加厉', '厉行节约', '约定俗成', '成仁取义', '义形于色', '色色俱全', '全军覆灭', '灭此朝食',
            '食日万钱', '钱可通神', '神施鬼设', '设身处地', '跃跃欲试',
            '地平天成', '成年累月', '月白风清', '清净无为', '为期不远', '远交近攻', '攻其无备', '备多力分', '分寸之末', '末学肤受',
            '受宠若惊', '惊涛骇浪', '浪子回头', '头疼脑热', '热火朝天', '天高地厚', '厚貌深情', '情同骨肉', '肉眼惠眉', '眉来眼去', '去伪存真', '真脏实犯', '犯上作乱', '乱头粗服',
            '服低做小', '小试锋芒', '芒刺在背', '背井离乡', '乡壁虚造', '造化小儿', '儿女情长', '长歌当哭', '哭天抹泪', '泪干肠断',
            '断鹤续凫', '凫趋雀跃', '跃然纸上', '上树拔梯', '梯山航海', '海枯石烂', '烂若披锦', '锦绣前程', '程门立雪', '雪虐风饕', '饕餮之徒', '徒劳无功', '功败垂成', '成千上万',
            '万象森罗', '罗雀掘鼠', '鼠窃狗盗', '盗憎主人', '人莫予毒', '毒手尊前', '前因后果', '果于自信', '信赏必罚', '罚不当罪',
            '罪恶昭彰', '彰善瘅恶', '恶贯满盈', '盈科后进', '进退两难', '难分难解', '解甲归田', '田月桑时', '时和年丰', '丰取刻与', '与世偃仰', '仰人鼻息', '息息相通', '通权达变',
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
            '井中视星', '星旗电戟', '戟指怒目', '目指气使', '使羊将狼', '狼心狗肺', '肺石风清', '清夜扪心', '心织笔耕',
            '耕当问奴', '奴颜婢膝', '膝痒搔背', '背信弃义', '义无反顾', '顾全大局', '局促不安',
            '安步当车', '车载斗量', '量才而为', '为渊驱鱼', '鱼游釜中', '中馈犹虚', '虚有其表', '表里如一', '一呼百诺',
            '诺诺连声', '声罪致讨', '讨价还价', '价增一顾', '顾盼自雄', '雄心壮志', '志美行厉',
            '厉兵秣马', '厉兵秣马', '速战速决', '决一雌雄', '雄才大略', '略见一斑', '斑驳陆离', '离弦走板', '板上钉钉',
            '钉嘴铁舌', '舌桥不下', '下马看花', '花样翻新', '新陈代谢', '谢天谢地', '地久天长',
            '长枕大被', '被山带河', '油腔滑调', '调兵遣将', '将伯之助', '助人为乐', '乐而不淫', '淫词艳曲', '曲终奏雅',
            '雅俗共赏', '赏罚分明', '明刑不戮', '戮力同心', '心心相印', '印累绶若', '若有所失',
            '失张失智', '智圆行方', '方枘圆凿', '凿凿有据', '据为己有', '有眼无珠', '珠光宝气', '气味相投', '投鼠忌器',
            '器宇轩昂', '昂首阔步', '步履维艰', '艰苦卓绝', '绝少分甘', '甘雨随车', '车水马龙',
            '龙飞凤舞', '舞衫歌扇', '扇枕温被', '被发缨冠', '冠冕堂皇', '皇天后土', '土阶茅屋', '屋乌之爱', '爱莫能助',
            '助我张目', '目挑心招', '发凡起例', '事必躬亲', '亲如骨肉', '肉跳心惊', '惊弓之鸟',
            '鸟枪换炮', '龙蛇飞动', '动人心弦', '弦外之音', '音容笑貌', '貌合心离', '离心离德', '德高望重', '重蹈覆辙',
            '辙乱旗靡', '靡靡之音', '音容宛在', '在所难免', '免开尊口', '口耳之学', '学而不厌',
            '厌难折冲', '冲口而出', '出谷迁乔', '乔龙画虎', '虎踞龙盘', '盘马弯弓', '弓折刀尽', '尽善尽美', '美意延年',
            '年高望重', '重温旧梦', '梦寐以求', '求全之毁', '毁家纾难', '难言之隐', '隐恶扬善',
            '善始善终', '终南捷径', '径情直行', '行成于思', '思潮起伏', '伏低做小', '小恩小惠', '惠而不费', '费尽心机',
            '机关算尽', '尽忠报国', '国士无双', '双宿双飞', '飞灾横祸', '祸从天降', '降格以求',
            '求同存异', '异名同实', '实至名归', '归真反璞', '璞玉浑金', '金玉锦绣', '绣花枕头', '头没杯案', '案牍劳形',
            '舌锋如火', '火伞高张', '张冠李戴', '戴月披星', '星移斗转', '转祸为福', '福至心灵',
            '灵丹圣药', '药笼中物', '物以类聚', '聚蚊成雷', '雷厉风行', '行将就木', '木本水源', '源源不断', '断烂朝报',
            '报冰公事', '事预则立', '立身处世', '世外桃源', '源源不绝', '绝甘分少', '少不经事',
            '事不师古', '兵连祸结', '结结巴巴', '巴三览四', '四面楚歌', '歌功颂德', '德厚流光', '光阴似箭', '箭在弦上',
            '上好下甚', '甚嚣尘上', '上下交困', '困知勉行', '行若无事', '事倍功半', '半夜三更',
            '更仆难数', '数见不鲜', '鲜车怒马', '马革裹尸', '尸居余气', '气冲牛斗', '斗筲之器', '盈盈一水', '水陆杂陈',
            '陈规陋习', '习焉不察', '察察为明', '明知故问', '问道于盲', '盲人摸象', '象齿焚身',
            '身不由主', '主客颠倒', '倒凤颠鸾', '鸾翔凤集', '集苑集枯', '枯木逢春', '春山如笑', '笑里藏刀', '刀山火海',
            '海外奇谈', '谈笑封侯', '侯门如海', '海阔天空', '空室清野', '野草闲花', '花颜月貌',
            '貌合神离', '离乡背井', '井蛙之见', '见仁见智', '智勇双全', '全受全归', '归马放牛', '牛骥同皂', '皂白不分',
            '分香卖履', '履舄交错', '错彩镂金', '金城汤池', '池鱼之殃', '殃及池鱼', '鱼烂而亡', '亡羊补牢', '牢不可破',
            '破颜微笑',
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
            '忘乎所以',
            '以指挠沸', '沸反盈天', '天上石麟', '麟趾呈祥', '祥麟威凤', '凤凰来仪', '仪静体闲', '闲云野鹤', '鹤发鸡皮',
            '皮里春秋', '秋风过耳', '耳食之谈', '谈笑自若', '谈笑自若', '若明若暗', '暗气暗恼', '恼羞成怒', '怒目而视', '视民如伤',
            '伤弓之鸟', '鸟语花香', '香花供养', '养痈成患', '患难与共', '共枝别干', '干卿底事', '事出有因', '因敌取资',
            '资深望重', '重睹天日', '日上三竿', '竿头直上', '上援下推', '推襟送抱', '抱蔓摘瓜', '绝处逢生', '多才多艺', '深恶痛绝',
            '腾蛟起凤', '历历可数', '数白论黄', '黄袍加身', '身外之物', '物换星移', '移樽就教', '教学相长', '长年累月',
            '月晕而风', '风流倜傥', '傥来之物', '物是人非', '非池中物', '物极必返', '反经行权', '权宜之计', '计出万全', '全无心肝', '肝肠寸断',
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
        self.waitAnswer()
        bodyTemplate = BodyTemplate1()
        bodyTemplate.setBackGroundImage('http://dbp-resource.gz.bcebos.com/530c5773-9c9b-671c-6212-4af927f1455a/%E6%8A%80%E8%83%BD%E5%BC%80%E5%A7%8B%E9%A1%B5%E8%83%8C%E6%99%AF.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-07T04%3A26%3A33Z%2F-1%2F%2F5cca0655decbf96a8b6a6d2602d240e4a7376df72228e3d404f218c603949e42')
        bodyTemplate.setPlainTextContent(r'欢迎来到成语大师，你可以在这里跟我一起玩很多关于成语的东西，这里有成语接龙、猜成语、成语故事，试着对我说，我要玩成语接龙')

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'欢迎来到成语大师，你可以在这里跟我一起玩很多关于成语的东西，这里有成语接龙、猜成语、成语故事，试着对我说，我要玩成语接龙'
        }

    def start_IdiomC(self):

        """
        成语接龙
        :return:
        """
        self.waitAnswer()
        rand_id = random.randint(0, 1000)
        idiom = self.idiom
        give_idiom = idiom[rand_id]

        self.setSessionAttribute("answer", give_idiom[-1], 0)
        self.setSessionAttribute("give_idiom", give_idiom, 0)
        self.setSessionAttribute("game_type", 'IdiomC', 0)
        self.setSessionAttribute("round_num", 1, 1)

        bodyTemplate = BodyTemplate1()
        bodyTemplate.setBackGroundImage('http://dbp-resource.gz.bcebos.com/530c5773-9c9b-671c-6212-4af927f1455a/%E6%8A%80%E8%83%BD%E5%BC%80%E5%A7%8B%E9%A1%B5%E8%83%8C%E6%99%AF.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-07T04%3A26%3A33Z%2F-1%2F%2F5cca0655decbf96a8b6a6d2602d240e4a7376df72228e3d404f218c603949e42')
        bodyTemplate.setPlainTextContent(r'我先来，我出：' + give_idiom)

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'我先来，我出' + give_idiom
        }

    def start_IdiomStory(self):

        """
        成语故事
        :return:
        """
        self.waitAnswer()
        user_story = self.getSlots('idiom_story_dict')
        idiom_story = self.idiom_story[user_story][0]

        self.setSessionAttribute("idiom_story_name", user_story, 0)
        self.setSessionAttribute("game_type", 'IdiomStory', 0)

        bodyTemplate = BodyTemplate1()
        bodyTemplate.setBackGroundImage(self.idiom_story[user_story][1])
        bodyTemplate.setPlainTextContent(r'好的，我们来听：' + user_story +  '，，，' + idiom_story + '还想再听一遍吗，试着对我说：再来一遍')

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'好的，我们来听：' + user_story +  '，，，' + idiom_story + '还想再听一遍吗，试着对我说，再来一遍'
        }

    def start_IdiomGuess(self):

        """
        成语故事
        :return:
        """
        self.waitAnswer()
        mode = self.getSlots('guess_mode')
        if mode == 'blank':

            self.setSessionAttribute("real_answer", answer, 0)
            self.setSessionAttribute("game_type", 'IdiomStory', 0)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.setBackGroundImage(self.idiom_story[user_story][1])
            bodyTemplate.setPlainTextContent(r'好的，我们来听：' + user_story + '，，，' + idiom_story + '还想再听一遍吗，试着对我说：再来一遍')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，我们来听：' + user_story + '，，，' + idiom_story + '还想再听一遍吗，试着对我说，再来一遍'
            }
        elif mode == 'scene':

            self.setSessionAttribute("idiom_story_name", user_story, 0)
            self.setSessionAttribute("game_type", 'IdiomStory', 0)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.setBackGroundImage(self.idiom_story[user_story][1])
            bodyTemplate.setPlainTextContent(r'好的，我们来听：' + user_story + '，，，' + idiom_story + '还想再听一遍吗，试着对我说：再来一遍')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，我们来听：' + user_story + '，，，' + idiom_story + '还想再听一遍吗，试着对我说，再来一遍'
            }
        elif mode == 'mode':

            self.setSessionAttribute("idiom_story_name", user_story, 0)
            self.setSessionAttribute("game_type", 'IdiomStory', 0)

            bodyTemplate = BodyTemplate1()
            bodyTemplate.setBackGroundImage(self.idiom_story[user_story][1])
            bodyTemplate.setPlainTextContent(r'好的，我们来听：' + user_story + '，，，' + idiom_story + '还想再听一遍吗，试着对我说：再来一遍')

            directive = RenderTemplate(bodyTemplate)
            return {
                'directives': [directive],
                'outputSpeech': r'好的，我们来听：' + user_story + '，，，' + idiom_story + '还想再听一遍吗，试着对我说，再来一遍'
            }



    def answer_helper(self):

        """
        提示
        :return:
        """
        self.waitAnswer()
        answer = self.getSessionAttribute("answer", 0)
        give_idiom = self.getSessionAttribute("give_idiom", 0)
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

            return {
                'outputSpeech': r'诶呀，提示不见了，努力想想吧'
            }

        else:

            card = TextCard(r'给你前两个字，想想：' + helper_idiom + '**' + '，如果实在想不到，可以对我说“跳过”')
            return {
                'card': card,
                'outputSpeech': r'给你前两个字，想想,' + helper_idiom + '如果实在想不到，可以对我说，跳过，'
            }

    def round(self):

        """
        读取轮回
        :return:
        """
        self.waitAnswer()
        return {
            'outputSpeech': r'您现在已经跟我大战第' + self.getSessionAttribute("idiom_num", 1) + '回合了'
        }

    def c_game(self):

        """
        继续游戏
        :return:
        """
        self.waitAnswer()
        give_idiom = self.getSessionAttribute("give_idiom", '')
        bodyTemplate = BodyTemplate1()
        bodyTemplate.setBackGroundImage(
            'http://dbp-resource.gz.bcebos.com/530c5773-9c9b-671c-6212-4af927f1455a/%E6%8A%80%E8%83%BD%E5%BC%80%E5%A7%8B%E9%A1%B5%E8%83%8C%E6%99%AF.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-07T04%3A26%3A33Z%2F-1%2F%2F5cca0655decbf96a8b6a6d2602d240e4a7376df72228e3d404f218c603949e42')
        bodyTemplate.setPlainTextContent(r'好的，我们继续，我刚刚出了：' + give_idiom)

        directive = RenderTemplate(bodyTemplate)
        return {
            'directives': [directive],
            'outputSpeech': r'好的，我们继续，我刚刚出了' + give_idiom
        }

    def answer(self):

        """
        回答
        :return:
        """
        self.waitAnswer()
        result = self.getSlots('idiom')
        try:
            user_answer = json.loads(result)
            user_answer = user_answer.get("origin")
        except:
            user_answer = result
        if not user_answer:
            self.nlu.ask('idiom')
        else:
            pass
        real_answer = self.getSessionAttribute("give_idiom", 0)
        answer = self.getSessionAttribute("answer", 0)
        a = 0

        if user_answer[0] != real_answer[3]:
            return {
                'outputSpeech': r'接错了哦，我的是，' + real_answer + '，哦！需要提示可以对我说，我需要提示，'
            }
        else:
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
            if new_give_idiom == None or new_give_idiom == '':
                return {
                    'outputSpeech': '诶呀，你这下真的打败我了，我输了，对我说，你重新开始，试试'
                }
            else:
                self.setSessionAttribute("answer", new_give_idiom[-1], '')
                self.setSessionAttribute("give_idiom", new_give_idiom, '')
                self.setSessionAttribute("round_num", self.getSessionAttribute("round_num", 1) + 1, 1)

                bodyTemplate = BodyTemplate1()
                bodyTemplate.setBackGroundImage(
                    'http://dbp-resource.gz.bcebos.com/530c5773-9c9b-671c-6212-4af927f1455a/%E6%8A%80%E8%83%BD%E5%BC%80%E5%A7%8B%E9%A1%B5%E8%83%8C%E6%99%AF.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-07T04%3A26%3A33Z%2F-1%2F%2F5cca0655decbf96a8b6a6d2602d240e4a7376df72228e3d404f218c603949e42')
                bodyTemplate.setPlainTextContent(r'你真棒，被你接到了，那我接：' + new_give_idiom)

                directive = RenderTemplate(bodyTemplate)
                return {
                    'directives': [directive],
                    'outputSpeech': r'你真棒，被你接到了，那我接，' + new_give_idiom
                }

    def quesheng(self):
        
            """
            缺省
            :return:
            """
            self.waitAnswer()
            try:
                text = self.data['request']['query']['original']
            except:
                return {
                    'outputSpeech': r'我没有理解您的意思'
                }
            else:
                if len(text) == 4:
                    return {
                        'outputSpeech': r'很抱歉，您回答的成语我没能理解哦'
                    }
                elif '下一关' in text or '不会' in text:

                    rand_id = random.randint(0, 499)
                    give_idiom = self.idiom[rand_id]

                    self.setSessionAttribute("answer", give_idiom[-1], 0)
                    self.setSessionAttribute("give_idiom", give_idiom, 0)
                    self.setSessionAttribute("round_num", self.getSessionAttribute("round_num", '') + 1, 1)

                    bodyTemplate = BodyTemplate1()
                    bodyTemplate.setBackGroundImage(
                        'http://dbp-resource.gz.bcebos.com/530c5773-9c9b-671c-6212-4af927f1455a/%E6%8A%80%E8%83%BD%E5%BC%80%E5%A7%8B%E9%A1%B5%E8%83%8C%E6%99%AF.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-07-07T04%3A26%3A33Z%2F-1%2F%2F5cca0655decbf96a8b6a6d2602d240e4a7376df72228e3d404f218c603949e42')
                    bodyTemplate.setPlainTextContent(r'好吧，要加油哦，那接下来我出：' + give_idiom)

                    directive = RenderTemplate(bodyTemplate)
                    return {
                        'directives': [directive],
                        'outputSpeech': r'好吧，要加油哦，那接下来我出' + give_idiom
                    }
                else:
                    return {
                        'outputSpeech': r'您说的我没有理解，对不起'
                    }
