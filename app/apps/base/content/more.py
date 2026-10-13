"""Новые материалы (для команды seed_more). Кортежи — (ky, ru, en)."""

ARTICLES = [
    # ------------------------------------------------------------------ nature
    {'slug': 'snow-leopard', 'category': ('discover', 'nature'), 'layout': 'standard',
     'title': ('Илбирс — тоолордун жашыруун ээси', 'Снежный барс — призрак гор', 'The snow leopard — ghost of the mountains'),
     'summary': (
         'Илбирс бийик тоолордо жашайт, аны көрүү абдан кыйын. Ал — сейрек жаныбар жана Бишкектин символу.',
         'Снежный барс живёт высоко в горах, и увидеть его очень трудно. Это редкий зверь и символ Бишкека.',
         'The snow leopard lives high in the mountains and is very hard to spot. It is a rare animal and a symbol of Bishkek.',
     ),
     'body': (
         '''<p><strong>Илбирс</strong> — бийик тоолордо жашаган чоң, тактуу мышык. Кыргызстанда ал Теңир-Тоодо жана Памир-Алайда жашайт.</p>
<h2>Эмне үчүн аны «жашыруун» дешет?</h2>
<p>Илбирс абдан сак жаныбар. Анын кара тактары бар боз-ак жүнү кар менен таштардын арасында дээрлик билинбейт. Окумуштуулар илбирс тууралуу көбүнчө изинен жана фотокапкандардан билишет. Фотокапкан — жаныбар жанынан өткөндө өзү сүрөткө тартып алган камера.</p>
<h2>Илбирс тоодо кантип жашайт?</h2>
<ul>
<li><strong>Калың жүнү</strong> катуу суукта жылытат.</li>
<li><strong>Кең таманы</strong> карга батып кетпөөгө жардам берет.</li>
<li><strong>Узун, жумшак куйругу</strong> аскада тең салмакты кармоого жардам берет. Уктаганда илбирс куйругуна жууркандай оронот.</li>
</ul>
<p>Илбирс тоо текелерге жана башка жапайы жаныбарларга аңчылык кылат.</p>
<h2>Сейрек жана корголгон</h2>
<p>Дүйнөдө илбирстер аз калды. Кыргызстанда ал Кызыл китепке киргизилген, ага аңчылык кылууга тыюу салынган. Илбирсти коруктарда коргошот, ал эми окумуштуулар тоодо канча илбирс жашаарын байкап турушат.</p>
<h2>Бишкектин символу</h2>
<p>Илбирс Бишкектин гербинде сүрөттөлгөн. Кыргыздар үчүн илбирс — күчтүн, эрдиктин жана тектүүлүктүн белгиси.</p>
<blockquote>Ойлонуп көр: кар менен аскалардын арасында жашаган жаныбарга көзгө көрүнбөө эмне үчүн пайдалуу?</blockquote>''',
         '''<p><strong>Снежный барс</strong>, или ирбис, по-кыргызски — <strong>илбирс</strong>. Это большая пятнистая кошка, которая живёт высоко в горах. В Кыргызстане его можно встретить в Тянь-Шане и Памиро-Алае.</p>
<h2>Почему «призрак гор»</h2>
<p>Барс очень осторожный и скрытный. Его серовато-белая шерсть с тёмными пятнами сливается со снегом и камнями, поэтому увидеть зверя почти невозможно. Учёные чаще всего узнают о барсах по следам и по снимкам фотоловушек — камер, которые сами делают снимок, когда рядом проходит животное.</p>
<h2>Как барс живёт в горах</h2>
<ul>
<li><strong>Густая шерсть</strong> согревает в сильные морозы.</li>
<li><strong>Широкие лапы</strong> работают как снегоступы и не дают провалиться в снег.</li>
<li><strong>Длинный пушистый хвост</strong> помогает держать равновесие на скалах. Во сне барс укрывается им, как одеялом.</li>
</ul>
<p>Барс охотится на горных козлов — тоо теке — и других диких животных.</p>
<h2>Редкий и охраняемый</h2>
<p>Снежных барсов в мире осталось немного. В Кыргызстане он занесён в Красную книгу, охотиться на него запрещено. Барса охраняют в заповедниках, а учёные следят за тем, сколько зверей живёт в горах.</p>
<h2>Символ Бишкека</h2>
<p>Снежный барс изображён на гербе Бишкека. Для кыргызов илбирс — символ силы, смелости и благородства.</p>
<blockquote>Подумай: почему животному, которое живёт среди снега и скал, полезно быть незаметным?</blockquote>''',
         '''<p>The <strong>snow leopard</strong>, called <strong>ilbirs</strong> in Kyrgyz, is a big spotted cat that lives high in the mountains. In Kyrgyzstan it is found in the Tian Shan and the Pamir-Alai.</p>
<h2>Why “the ghost of the mountains”?</h2>
<p>The snow leopard is very shy and careful. Its greyish-white fur with dark spots blends in with snow and rocks, so it is almost impossible to see. Scientists usually learn about snow leopards from their tracks and from camera traps — cameras that take a picture by themselves when an animal walks past.</p>
<h2>How it survives in the mountains</h2>
<ul>
<li><strong>Thick fur</strong> keeps it warm in hard frosts.</li>
<li><strong>Wide paws</strong> work like snowshoes, so it does not sink into the snow.</li>
<li><strong>A long fluffy tail</strong> helps it keep its balance on rocks. When it sleeps, it wraps the tail around itself like a blanket.</li>
</ul>
<p>The snow leopard hunts mountain goats (ibex) and other wild animals.</p>
<h2>Rare and protected</h2>
<p>There are not many snow leopards left in the world. In Kyrgyzstan it is listed in the Red Book, and hunting it is forbidden. Snow leopards are protected in nature reserves, and scientists keep track of how many live in the mountains.</p>
<h2>A symbol of Bishkek</h2>
<p>The snow leopard appears on the coat of arms of Bishkek. For the Kyrgyz people, the ilbirs is a symbol of strength, courage and nobility.</p>
<blockquote>Think about it: why is it useful for an animal that lives among snow and rocks to be hard to see?</blockquote>''',
     ),
     'facts': [
         ('Илбирс арстан же жолборстой күркүрөй албайт.', 'Снежный барс не умеет рычать, как лев или тигр.', 'A snow leopard cannot roar like a lion or a tiger.'),
         ('Илбирстин куйругу дээрлик денесиндей узун.', 'Хвост барса почти такой же длинный, как его тело.', 'A snow leopard’s tail is almost as long as its body.'),
     ]},

    {'slug': 'why-so-many-mountains', 'category': ('discover', 'nature'), 'layout': 'standard',
     'title': ('Эмне үчүн Кыргызстанда тоолор көп?', 'Почему в Кыргызстане так много гор', 'Why Kyrgyzstan has so many mountains'),
     'summary': (
         'Кыргызстандын көпчүлүк бөлүгүн тоолор ээлейт. Алар кантип пайда болгонун билебиз.',
         'Горы занимают большую часть Кыргызстана. Разбираемся, откуда они взялись и где живут люди.',
         'Mountains cover most of Kyrgyzstan. Let’s find out where they came from and where people live.',
     ),
     'body': (
         '''<p>Кыргызстандын картасын карачы: ал дээрлик толугу менен күрөң түстө. Картада тоолор ушундай белгиленет. Тоолор өлкөнүн аймагынын 90 пайыздан ашыгын ээлейт, ошондуктан Кыргызстанды тоолуу өлкө деп аташат.</p>
<h2>Эки чоң тоо системасы</h2>
<ul>
<li><strong>Теңир-Тоо</strong> (Тянь-Шань) өлкөнүн көпчүлүк бөлүгүн ээлейт.</li>
<li><strong>Памир-Алай</strong> — түштүктөгү тоолор, Тажикстан менен чек арада.</li>
</ul>
<h2>Тоолор кантип пайда болгон?</h2>
<p>Жердин кабыгы абдан жай жылган чоң плиталардан турат. Алыскы түштүктө Индия плитасы Евразия плитасын түртүп турат. Ушул басымдан жер бырышып, өйдө көтөрүлөт — тоолор ушинтип өсөт. Бул миллиондогон жылдардан бери уланып келет жана азыр да токтой элек. Ошондуктан Кыргызстанда кээде жер титирөө болот.</p>
<h2>Эң бийик чокулар</h2>
<ul>
<li><strong>Жеңиш чокусу</strong> — 7439 метр. Бул Кыргызстандын эң бийик чекити, Кытай менен чек арада жайгашкан.</li>
<li><strong>Ленин чокусу</strong> — 7134 метр, Памир-Алайда.</li>
</ul>
<h2>Адамдар кайда жашайт?</h2>
<p>Тоо кыркаларынын ортосунда өрөөндөр жатат: Чүй, Талас өрөөндөрү, Ысык-Көл ойдуңу жана Фергана өрөөнүнүн чети. Ал жерде жылуураак, суу жана түшүмдүү жер бар, ошондуктан шаарлар менен айылдардын көбү өрөөндөрдө. Ал эми жайында малчылар малын бийик тоодогу жайлоолорго айдап чыгышат.</p>
<blockquote>Кыргызстандын картасынан Теңир-Тоону жана Памир-Алайды тап. Кайсынысы сенин үйүңө жакыныраак?</blockquote>''',
         '''<p>Посмотри на карту Кыргызстана: она почти вся коричневая — так на картах обозначают горы. Горы занимают больше 90% территории страны, поэтому Кыргызстан называют горной страной.</p>
<h2>Две большие горные системы</h2>
<ul>
<li><strong>Тянь-Шань</strong> (по-кыргызски — Теңир-Тоо) занимает большую часть страны.</li>
<li><strong>Памиро-Алай</strong> — горы на юге, на границе с Таджикистаном.</li>
</ul>
<h2>Откуда взялись горы</h2>
<p>Земная кора состоит из огромных плит, которые очень медленно движутся. Далеко на юге Индийская плита давит на Евразийскую. От этого давления земля сминается в складки и поднимается — так растут горы. Это продолжается миллионы лет и не закончилось до сих пор. Поэтому в Кыргызстане иногда бывают землетрясения.</p>
<h2>Самые высокие вершины</h2>
<ul>
<li><strong>Жеңиш чокусу</strong> (пик Победы) — 7439 метров. Это самая высокая точка Кыргызстана, она находится на границе с Китаем.</li>
<li><strong>Пик Ленина</strong> — 7134 метра, в Памиро-Алае.</li>
</ul>
<h2>Где живут люди</h2>
<p>Между хребтами лежат долины: Чуйская, Таласская, котловина Иссык-Куля и край Ферганской долины. Там теплее, есть вода и плодородная земля, поэтому большинство городов и сёл находится в долинах. А летом чабаны поднимаются со стадами на высокогорные пастбища — жайлоо.</p>
<blockquote>Найди на карте Кыргызстана Тянь-Шань и Памиро-Алай. Какие горы ближе к твоему дому?</blockquote>''',
         '''<p>Look at a map of Kyrgyzstan: it is almost all brown — that is how maps show mountains. Mountains cover more than 90% of the country, which is why Kyrgyzstan is called a mountain country.</p>
<h2>Two great mountain systems</h2>
<ul>
<li><strong>The Tian Shan</strong> (Teñir-Too in Kyrgyz) covers most of the country.</li>
<li><strong>The Pamir-Alai</strong> is in the south, along the border with Tajikistan.</li>
</ul>
<h2>Where did the mountains come from?</h2>
<p>The Earth’s crust is made of huge plates that move very slowly. Far to the south, the Indian plate pushes against the Eurasian plate. This pressure crumples the land into folds and lifts it up — that is how mountains grow. It has been happening for millions of years and is still going on. That is why Kyrgyzstan sometimes has earthquakes.</p>
<h2>The highest peaks</h2>
<ul>
<li><strong>Jengish Chokusu</strong> (Victory Peak) — 7,439 metres. It is the highest point of Kyrgyzstan, on the border with China.</li>
<li><strong>Lenin Peak</strong> — 7,134 metres, in the Pamir-Alai.</li>
</ul>
<h2>Where do people live?</h2>
<p>Between the ranges lie valleys: the Chuy and Talas valleys, the Issyk-Kul basin and the edge of the Fergana Valley. They are warmer and have water and fertile land, so most towns and villages are in the valleys. In summer, herders take their animals up to high mountain pastures called jailoo.</p>
<blockquote>Find the Tian Shan and the Pamir-Alai on a map of Kyrgyzstan. Which mountains are closer to your home?</blockquote>''',
     ),
     'facts': [
         ('«Тянь-Шань» деген аталыш «Асман тоолору» дегенди билдирет.', 'Название «Тянь-Шань» означает «Небесные горы».', 'The name “Tian Shan” means “Heavenly Mountains”.'),
     ]},

    {'slug': 'glaciers-water-tanks', 'category': ('discover', 'nature'), 'layout': 'standard',
     'title': ('Мөңгүлөр — Кыргызстандын суу кампалары', 'Ледники — водяные баки Кыргызстана', 'Glaciers — the water tanks of Kyrgyzstan'),
     'summary': (
         'Тоолордогу муз дарыяларды кантип суу менен камсыз кылат?',
         'Как лёд высоко в горах наполняет водой реки Кыргызстана.',
         'How ice high in the mountains fills the rivers of Kyrgyzstan with water.',
     ),
     'body': (
         '''<p><strong>Мөңгү</strong> — бийик тоолордо кылымдар бою жаткан чоң муз катмары. Кыргызстандын тоолорунда миңдеген мөңгүлөр бар.</p>
<h2>Мөңгү кантип пайда болот?</h2>
<p>Бийик тоодо жайында да суук болот, кар эрип үлгүрбөйт. Жыл сайын жаңы кар эски кардын үстүнө түшүп, аны басат, акырындап кар катуу музга айланат. Мөңгү өз салмагынан улам өрөөн боюнча өтө жай ылдый жылат — абдан коюу дарыя сыяктуу.</p>
<h2>Эмне үчүн мөңгүлөр — «суу кампалары»?</h2>
<p>Кышында мөңгүлөр менен кар сууну топтойт, ал эми жайдын ысыгында эрийт. Эриген суу булак болуп агып, тоо дарыяларын толтурат. Ошондуктан Кыргызстандын көп дарыялары муз эриген жай айларында эң толук агат.</p>
<h2>Нарын дарыясы</h2>
<p>Кыргызстандын эң чоң дарыясы — <strong>Нарын</strong>. Ал Теңир-Тоодон башталат, аны мөңгүлөр жана кар суусу азыктандырат. Нарында гидроэлектростанциялар курулган, мисалы, Токтогул ГЭСи: суу турбиналарды айлантып, электр энергиясын берет. Андан ары Нарын Кара-Дарыя менен кошулуп, Сыр-Дарыяны түзөт.</p>
<h2>Мөңгүлөрдү коргоо керек</h2>
<p>Климат жылыгандыктан дүйнөдөгү, анын ичинде Кыргызстандагы көп мөңгүлөр кичирейип баратат. Мөңгүлөрдү изилдеген окумуштуулар — гляциологдор аларды өлчөп, келечекте дарыяларда канча суу болоорун түшүнүүгө аракет кылышат.</p>
<blockquote>Тажрыйба жаса: табакка бир кесим муз сал да, ал эригенде канча суу чыгарын карап көр.</blockquote>''',
         '''<p><strong>Ледник</strong> (по-кыргызски — <strong>мөңгү</strong>) — это огромная масса льда, которая веками лежит высоко в горах. В горах Кыргызстана тысячи ледников.</p>
<h2>Как появляется ледник</h2>
<p>Высоко в горах даже летом холодно, и снег не успевает растаять. Год за годом новый снег ложится на старый и придавливает его, и постепенно снег превращается в плотный лёд. Под собственным весом ледник очень медленно сползает вниз по долине — как очень густая река.</p>
<h2>Почему ледники — «водяные баки»</h2>
<p>Зимой ледники и снег копят воду, а в летнюю жару тают. Талая вода стекает ручьями и наполняет горные реки. Поэтому многие реки Кыргызстана полноводнее всего летом, когда тает лёд.</p>
<h2>Река Нарын</h2>
<p>Самая большая река Кыргызстана — <strong>Нарын</strong>. Она начинается в горах Тянь-Шаня, её питают ледники и снега. На Нарыне построены гидроэлектростанции, например Токтогульская ГЭС: вода вращает турбины и даёт электричество. Дальше Нарын сливается с Карадарьёй и образует Сырдарью.</p>
<h2>Ледники надо беречь</h2>
<p>Из-за потепления климата многие ледники в мире, в том числе в Кыргызстане, становятся меньше. Учёные-гляциологи измеряют ледники, чтобы понять, сколько воды будет в реках в будущем.</p>
<blockquote>Проведи опыт: положи кусок льда в тарелку и посмотри, сколько воды получится, когда он растает.</blockquote>''',
         '''<p>A <strong>glacier</strong> (<strong>möngü</strong> in Kyrgyz) is a huge mass of ice that lies high in the mountains for hundreds of years. The mountains of Kyrgyzstan have thousands of glaciers.</p>
<h2>How a glacier forms</h2>
<p>High in the mountains it is cold even in summer, and the snow does not have time to melt. Year after year new snow falls on old snow and presses it down, and slowly the snow turns into hard ice. Under its own weight a glacier creeps very slowly down the valley — like a very thick river.</p>
<h2>Why glaciers are “water tanks”</h2>
<p>In winter, glaciers and snow store water, and in the summer heat they melt. Meltwater runs down in streams and fills the mountain rivers. That is why many rivers in Kyrgyzstan are fullest in summer, when the ice melts.</p>
<h2>The Naryn River</h2>
<p>The biggest river in Kyrgyzstan is the <strong>Naryn</strong>. It starts in the Tian Shan and is fed by glaciers and snow. Hydroelectric power stations have been built on the Naryn, such as the Toktogul station: the water turns turbines and makes electricity. Further on, the Naryn joins the Kara Darya to form the Syr Darya.</p>
<h2>Glaciers need care</h2>
<p>Because the climate is getting warmer, many glaciers around the world, including in Kyrgyzstan, are shrinking. Scientists called glaciologists measure glaciers to understand how much water rivers will have in the future.</p>
<blockquote>Try an experiment: put a piece of ice on a plate and see how much water you get when it melts.</blockquote>''',
     ),
     'facts': [
         ('Түштүк Эңилчек — Теңир-Тоодогу эң чоң мөңгүлөрдүн бири.', 'Южный Иныльчек — один из самых больших ледников Тянь-Шаня.', 'South Inylchek is one of the largest glaciers in the Tian Shan.'),
         ('Мөңгүлөрдү изилдеген окумуштууларды гляциологдор деп аташат.', 'Учёных, которые изучают ледники, называют гляциологами.', 'Scientists who study glaciers are called glaciologists.'),
     ]},

    # ---------------------------------------------------------------- culture
    {'slug': 'kyrgyz-hospitality-dastorkon', 'category': ('culture', 'holidays'), 'layout': 'standard',
     'title': ('Кыргыз меймандостугу: дасторкон', 'Кыргызское гостеприимство: дастархан', 'Kyrgyz hospitality: the dastorkon'),
     'summary': (
         'Конокту кантип тосушат, эмне үчүн нанды урматташат жана төргө ким отурат.',
         'Как встречают гостей, почему так берегут хлеб и кого сажают на почётное место.',
         'How guests are welcomed, why bread is treated with respect and who sits in the place of honour.',
     ),
     'body': (
         '''<p><strong>Дасторкон</strong> деп тамак-аш коюу үчүн жайылган кездемени жана конокко даярдалган бүт сыйды айтышат. Кыргыздар илгертен меймандос эл катары белгилүү: конок күтүүсүз келсе да, аны жылуу тосуп, сыйлашат.</p>
<h2>Дасторконго эмне коюлат?</h2>
<p>Адегенде дасторконго нан жана боорсок, таттуулар, мейиз, жаңгак жана, албетте, чай коюлат. Андан кийин ысык тамак берилет. Иш-чара канчалык маанилүү болсо, дасторкон ошончолук бай болот.</p>
<h2>Нан — дасторкондун башы</h2>
<ul>
<li>Нанды ыргытууга, жерге түшүрүүгө жана тескери коюуга болбойт.</li>
<li>Нанды көбүнчө бычак менен кеспей, кол менен сындырып, баарына бөлүп беришет.</li>
<li>Нандын күкүмүн ыргытып жиберишпейт.</li>
</ul>
<h2>Чай жана чыны</h2>
<p>Чайды чыныга куюшат. Адатта үй ээси чайды аз-аздан, чыныны толтурбай куюп, тез-тез кошуп турат. Ошентип конок ар дайым ысык чай ичет, ал эми үй ээси ага кубанычын билдирет.</p>
<h2>Улууларга урмат</h2>
<p>Эң урматтуу коноктор менен улууларды <strong>төргө</strong> — эшиктен эң алыс, сыйлуу орунга отургузушат. Тамакты адегенде улууларга жана конокторго беришет, ал эми кичүүлөр жардам берет: чай алып келет, идиш-аякты жыйнашат. Тамактан кийин улуу киши <strong>бата</strong> берет — үй ээлерине ак тилек айтат.</p>
<blockquote>Сенин үй-бүлөңдө конокторду кантип тосушат? Силердин салттар эмнеси менен окшош, эмнеси менен айырмаланат?</blockquote>''',
         '''<p><strong>Дастархан</strong> (по-кыргызски — <strong>дасторкон</strong>) — это скатерть, которую расстилают для угощения, и сам накрытый стол. Кыргызы издавна славятся гостеприимством: гостя всегда тепло встречают и угощают, даже если он пришёл неожиданно.</p>
<h2>Что ставят на дастархан</h2>
<p>Сначала на стол ставят хлеб и боорсоки, сладости, изюм, орехи и, конечно, чай. Потом подают горячие блюда. Чем важнее событие, тем богаче дастархан.</p>
<h2>Хлеб — главный на столе</h2>
<ul>
<li>Хлеб нельзя бросать, ронять на землю и класть вверх дном.</li>
<li>Лепёшку часто не режут ножом, а разламывают руками и раздают всем.</li>
<li>Хлебные крошки не выбрасывают.</li>
</ul>
<h2>Чай и пиала</h2>
<p>Чай наливают в пиалы — по-кыргызски <strong>чыны</strong>. Обычно хозяйка наливает чай понемногу, не до краёв, и часто подливает. Так у гостя всегда горячий чай, а хозяйка показывает, что рада ему.</p>
<h2>Старшим — почёт</h2>
<p>Самых уважаемых гостей и старших сажают на <strong>төр</strong> — почётное место дальше всего от входа. Угощение сначала подают старшим и гостям, а младшие помогают: приносят чай, убирают посуду. После еды старший даёт <strong>бата</strong> — благословение и добрые пожелания хозяевам.</p>
<blockquote>Как в твоей семье встречают гостей? Чем похожи и чем отличаются ваши обычаи?</blockquote>''',
         '''<p>A <strong>dastorkon</strong> is the cloth spread out for a meal — and the whole table laid out for guests. The Kyrgyz have long been known for their hospitality: a guest is always welcomed warmly and offered food, even if they arrive unexpectedly.</p>
<h2>What goes on the dastorkon</h2>
<p>First come bread and boorsok, sweets, raisins, nuts and, of course, tea. Hot dishes are served later. The more important the occasion, the richer the dastorkon.</p>
<h2>Bread comes first</h2>
<ul>
<li>Bread must not be thrown, dropped on the ground or laid upside down.</li>
<li>Flatbread is often not cut with a knife but broken by hand and shared with everyone.</li>
<li>Breadcrumbs are not thrown away.</li>
</ul>
<h2>Tea and the cup</h2>
<p>Tea is poured into small bowl-shaped cups called <strong>chyny</strong>. The host usually pours only a little, not to the brim, and tops it up often. That way the guest always has hot tea, and the host shows they are glad to have them.</p>
<h2>Respect for elders</h2>
<p>The most honoured guests and elders are seated at the <strong>tör</strong> — the place of honour farthest from the door. Food is served to elders and guests first, while younger people help by bringing tea and clearing dishes. After the meal an elder gives a <strong>bata</strong> — a blessing with good wishes for the hosts.</p>
<blockquote>How does your family welcome guests? How are your customs similar, and how are they different?</blockquote>''',
     ),
     'facts': [
         ('Боорсок — майрамдык дасторкондун милдеттүү тамагы.', 'Боорсоки — обязательное угощение на праздничном дастархане.', 'Boorsok is a must on a festive dastorkon.'),
     ]},

    # ------------------------------------------------------------ professions
    {'slug': 'doctor', 'category': ('modern', 'professions'), 'layout': 'profession',
     'title': ('Дарыгер', 'Врач', 'Doctor'),
     'summary': (
         'Дарыгер эмне кылат жана дарыгер болуу үчүн эмне керек.',
         'Чем занимается врач и что помогает им стать.',
         'What a doctor does and what helps you become one.',
     ),
     'body': (
         '''<p><strong>Дарыгер</strong> адамдарды дарылайт жана алардын ооруп калбашына жардам берет. Дарыгерлер ооруканаларда, тез жардамда, шаарларда жана алыскы тоолуу айылдарда иштешет.</p>
<h2>Кандай дарыгерлер болот?</h2>
<ul>
<li><strong>педиатр</strong> — балдар дарыгери;</li>
<li><strong>хирург</strong> операция жасайт;</li>
<li><strong>тиш дарыгери</strong> тиштерди дарылайт;</li>
<li><strong>тез жардам дарыгери</strong> кырсык болгон жерге биринчи жетет.</li>
</ul>
<h2>Эмне керек болот?</h2>
<p>Биология жана химия, көңүл буруу, чыдамкайлык жана боорукердик. Дарыгер адамды уга билиши жана кыйын учурда тынч аракет кылышы керек. Дарыгерликке узак окушат: университетте бир нече жыл, андан кийин ооруканада практика.</p>
<h2>Эмнеден баштаса болот?</h2>
<p>Адамдын денеси кантип түзүлгөнүн үйрөн, биринчи жардамдын негиздерин бил жана өз ден соолугуңа кам көр: жетиштүү укта, көп кыймылда жана туура тамактан.</p>''',
         '''<p><strong>Врач</strong> лечит людей и помогает им не болеть. Врачи работают в больницах и поликлиниках, на скорой помощи, в городах и в далёких горных сёлах.</p>
<h2>Какие бывают врачи</h2>
<ul>
<li><strong>педиатр</strong> — детский врач;</li>
<li><strong>хирург</strong> делает операции;</li>
<li><strong>стоматолог</strong> лечит зубы;</li>
<li><strong>врач скорой помощи</strong> первым приезжает туда, где случилась беда.</li>
</ul>
<h2>Что пригодится</h2>
<p>Биология и химия, внимательность, терпение и доброта. Врач должен уметь выслушать человека и спокойно действовать в трудной ситуации. Учиться на врача долго: несколько лет в университете, а потом практика в больнице.</p>
<h2>С чего начать</h2>
<p>Узнай, как устроено тело человека, изучи основы первой помощи и заботься о своём здоровье: высыпайся, больше двигайся и правильно питайся.</p>''',
         '''<p>A <strong>doctor</strong> treats people and helps them stay healthy. Doctors work in hospitals and clinics, on ambulances, in cities and in faraway mountain villages.</p>
<h2>Kinds of doctors</h2>
<ul>
<li>a <strong>paediatrician</strong> is a children’s doctor;</li>
<li>a <strong>surgeon</strong> performs operations;</li>
<li>a <strong>dentist</strong> takes care of teeth;</li>
<li>an <strong>ambulance doctor</strong> is the first to arrive when something bad happens.</li>
</ul>
<h2>What helps</h2>
<p>Biology and chemistry, attention to detail, patience and kindness. A doctor must be able to listen to people and stay calm in difficult moments. Training takes a long time: several years at university and then practice in a hospital.</p>
<h2>Where to start</h2>
<p>Learn how the human body works, study basic first aid and take care of your own health: get enough sleep, move a lot and eat well.</p>''',
     ),
     'facts': []},

    {'slug': 'engineer', 'category': ('modern', 'professions'), 'layout': 'profession',
     'title': ('Инженер', 'Инженер', 'Engineer'),
     'summary': (
         'Инженерлер көпүрөлөрдү, жолдорду, машиналарды жана электр станцияларын ойлоп табышат.',
         'Инженеры придумывают и строят мосты, дороги, машины и электростанции.',
         'Engineers design and build bridges, roads, machines and power stations.',
     ),
     'body': (
         '''<p><strong>Инженер</strong> илимдин жардамы менен адамдарга пайдалуу нерселерди ойлоп табат жана курат. Көпүрө, жол, лифт, телефон, электр станциясы — мунун баары инженерлердин эмгеги.</p>
<h2>Кандай инженерлер болот?</h2>
<ul>
<li><strong>куруучу инженер</strong> үйлөрдү, көпүрөлөрдү жана жолдорду долбоорлойт;</li>
<li><strong>энергетик</strong> электр станцияларында жана электр тармактарында иштейт;</li>
<li><strong>механик</strong> машиналарды жана станокторду түзөт;</li>
<li><strong>электроника инженери</strong> түзмөктөрдү жана роботторду жасайт.</li>
</ul>
<h2>Тоолуу өлкөдө инженер болуу</h2>
<p>Кыргызстанда инженерлер үчүн кызыктуу иш көп: тоо ашуулары аркылуу жол салуу, дарыяларга көпүрө куруу, тоо дарыяларынын күчү менен электр энергиясын алуу. Курулуштар жер титирөөгө чыдамдуу болушу керек — муну да инженерлер эсептешет.</p>
<h2>Эмне керек болот?</h2>
<p>Математика жана физика, сүрөт тартуу жана чийме түшүнүү, ошондой эле нерселердин кантип иштээрин билүүгө кызыгуу.</p>
<h2>Эмнеден баштаса болот?</h2>
<p>Конструктордон курулуштарды жаса, робототехника ийримине бар, эски буюмдарды чоңдор менен бирге ажыратып, ичинде эмне бар экенин карап көр.</p>''',
         '''<p><strong>Инженер</strong> с помощью науки придумывает и создаёт полезные для людей вещи. Мост, дорога, лифт, телефон, электростанция — всё это работа инженеров.</p>
<h2>Какие бывают инженеры</h2>
<ul>
<li><strong>инженер-строитель</strong> проектирует дома, мосты и дороги;</li>
<li><strong>энергетик</strong> работает на электростанциях и в электросетях;</li>
<li><strong>механик</strong> создаёт машины и станки;</li>
<li><strong>инженер-электронщик</strong> делает приборы и роботов.</li>
</ul>
<h2>Инженер в горной стране</h2>
<p>В Кыргызстане у инженеров много интересных задач: прокладывать дороги через горные перевалы, строить мосты через реки, получать электричество с помощью силы горных рек. Постройки должны выдерживать землетрясения — это тоже рассчитывают инженеры.</p>
<h2>Что пригодится</h2>
<p>Математика и физика, умение рисовать и читать чертежи и любопытство — желание понять, как всё работает.</p>
<h2>С чего начать</h2>
<p>Собирай конструкции из конструктора, запишись в кружок робототехники, вместе со взрослыми разбери старый ненужный прибор и посмотри, что у него внутри.</p>''',
         '''<p>An <strong>engineer</strong> uses science to design and build useful things for people. Bridges, roads, lifts, phones and power stations are all the work of engineers.</p>
<h2>Kinds of engineers</h2>
<ul>
<li>a <strong>civil engineer</strong> designs houses, bridges and roads;</li>
<li>a <strong>power engineer</strong> works at power stations and on electricity networks;</li>
<li>a <strong>mechanical engineer</strong> creates machines and tools;</li>
<li>an <strong>electronics engineer</strong> makes devices and robots.</li>
</ul>
<h2>An engineer in a mountain country</h2>
<p>Engineers in Kyrgyzstan have many interesting tasks: building roads over mountain passes and bridges across rivers, and making electricity from the power of mountain rivers. Buildings must be able to withstand earthquakes — engineers work that out too.</p>
<h2>What helps</h2>
<p>Maths and physics, being able to draw and read technical drawings, and curiosity — wanting to know how things work.</p>
<h2>Where to start</h2>
<p>Build models with a construction set, join a robotics club, and with an adult take apart an old, unneeded gadget to see what is inside.</p>''',
     ),
     'facts': []},

    {'slug': 'architect', 'category': ('modern', 'professions'), 'layout': 'profession',
     'title': ('Архитектор', 'Архитектор', 'Architect'),
     'summary': (
         'Архитектор имараттарды ойлоп табат. Боз үйдүн идеялары бүгүн да шыктандырат.',
         'Архитектор придумывает здания. И идеи юрты вдохновляют его до сих пор.',
         'An architect designs buildings — and the ideas of the yurt still inspire them today.',
     ),
     'body': (
         '''<p><strong>Архитектор</strong> имараттарды ойлоп табат: үйлөрдү, мектептерди, театрларды, стадиондорду, парктарды. Ал имарат кандай көрүнөрүн, ичи кандай болоорун жана адамдарга ыңгайлуу болушун ойлонот.</p>
<h2>Архитектор эмне кылат?</h2>
<ul>
<li>адамдарга кандай имарат керек экенин угат;</li>
<li>эскиз тартат, анан компьютерде так чиймелерди жасайт;</li>
<li>макет — имараттын кичинекей моделин түзөт;</li>
<li>инженерлер менен бирге имарат бекем жана коопсуз болушун карайт.</li>
</ul>
<h2>Боз үйдөн эмнени үйрөнсө болот?</h2>
<p>Боз үй — көчмөндөрдүн акылман ойлоп тапкан үйү. Ал жеңил, тез чогултулат жана ажыратылат, тегерек формасы шамалга жакшы туруштук берет, ал эми түндүк аркылуу үстүнөн жарык кирет. Азыркы архитекторлор да ушундай идеяларды колдонушат: тегерек имараттарды, үстүнөн жарык түшкөн күмбөздөрдү курушат, фасаддарды түндүк менен улуттук оюм-чийимдер менен кооздошот.</p>
<h2>Эмне керек болот?</h2>
<p>Сүрөт тартуу, математика жана геометрия, кооздукту сезүү жана адамдарга кам көрүү.</p>
<h2>Эмнеден баштаса болот?</h2>
<p>Өз шаарыңдагы же айылыңдагы имараттарды карап, кайсынысы жагарын жана эмне үчүн жагарын ойлон. Кагаздан же картондон үйдүн макетин жасап көр.</p>''',
         '''<p><strong>Архитектор</strong> придумывает здания: дома, школы, театры, стадионы, парки. Он думает о том, как здание будет выглядеть, как оно будет устроено внутри и насколько удобно в нём будет людям.</p>
<h2>Что делает архитектор</h2>
<ul>
<li>выясняет, какое здание нужно людям;</li>
<li>рисует эскизы, а потом делает точные чертежи на компьютере;</li>
<li>создаёт макет — маленькую модель здания;</li>
<li>вместе с инженерами следит, чтобы здание было прочным и безопасным.</li>
</ul>
<h2>Чему можно научиться у юрты</h2>
<p>Юрта — мудрое изобретение кочевников. Она лёгкая, быстро собирается и разбирается, круглая форма хорошо выдерживает ветер, а свет проходит сверху через түндүк. Современные архитекторы тоже используют такие идеи: строят круглые здания и купола со светом сверху, украшают фасады тюндюком и национальными орнаментами.</p>
<h2>Что пригодится</h2>
<p>Рисование, математика и геометрия, чувство красоты и забота о людях.</p>
<h2>С чего начать</h2>
<p>Присмотрись к зданиям в своём городе или селе: какие тебе нравятся и почему? Попробуй сделать макет дома из бумаги или картона.</p>''',
         '''<p>An <strong>architect</strong> designs buildings: houses, schools, theatres, stadiums and parks. They think about how a building will look, how it will be arranged inside and how comfortable it will be for people.</p>
<h2>What an architect does</h2>
<ul>
<li>finds out what kind of building people need;</li>
<li>draws sketches and then makes exact drawings on a computer;</li>
<li>builds a scale model of the building;</li>
<li>works with engineers to make sure the building is strong and safe.</li>
</ul>
<h2>What we can learn from the yurt</h2>
<p>The yurt is a clever invention of nomads. It is light, quick to put up and take down, its round shape stands up well to the wind, and light comes in from above through the tunduk. Modern architects use ideas like these too: they build round buildings and domes with light from above, and decorate facades with the tunduk and national ornaments.</p>
<h2>What helps</h2>
<p>Drawing, maths and geometry, a sense of beauty and caring about people.</p>
<h2>Where to start</h2>
<p>Look closely at the buildings in your town or village: which ones do you like, and why? Try making a model of a house from paper or card.</p>''',
     ),
     'facts': []},

    {'slug': 'scientist', 'category': ('modern', 'professions'), 'layout': 'profession',
     'title': ('Окумуштуу', 'Учёный', 'Scientist'),
     'summary': (
         'Окумуштуулар суроо берип, тажрыйба жасап, дүйнө тууралуу жаңы нерселерди ачышат.',
         'Учёные задают вопросы, ставят опыты и узнают о мире новое.',
         'Scientists ask questions, run experiments and discover new things about the world.',
     ),
     'body': (
         '''<p><strong>Окумуштуу</strong> — дүйнө кантип түзүлгөнүн изилдеген адам. Ал суроо берет, байкоо жүргүзөт, тажрыйба жасайт жана жоопту далилдер менен текшерет.</p>
<h2>Окумуштуу кантип иштейт?</h2>
<ol>
<li>Суроо берет: «Эмне үчүн мындай болот?»</li>
<li>Божомол айтат — болжолдуу жоопту ойлойт.</li>
<li>Тажрыйба же байкоо жүргүзүп, маалымат чогултат.</li>
<li>Божомол туура болгон-болбогонун текшерет жана жыйынтыгын башкалар менен бөлүшөт.</li>
</ol>
<h2>Кыргызстанда эмнени изилдешет?</h2>
<p>Изилдей турган нерсе абдан көп: мөңгүлөр жана дарыялар, жер титирөөлөр, Ысык-Көл, илбирс сыяктуу сейрек жаныбарлар, Улуу Жибек жолундагы байыркы шаарлар жана «Манас» эпосу. Өлкөдө Улуттук илимдер академиясы жана көп университеттер иштейт.</p>
<h2>Эмне керек болот?</h2>
<p>Билимге кызыгуу, чыдамкайлык, тактык жана жаңылуудан коркпоо: ар бир ийгиликсиз тажрыйба да бир нерсеге үйрөтөт.</p>
<h2>Эмнеден баштаса болот?</h2>
<p>Жаратылышты байкоо күндөлүгүн жүргүз, мектептин илимий долбоорлоруна жана олимпиадаларына катыш, кызыктуу суроолоруңду жазып жүр.</p>''',
         '''<p><strong>Учёный</strong> — это человек, который исследует, как устроен мир. Он задаёт вопросы, наблюдает, ставит опыты и проверяет ответы с помощью доказательств.</p>
<h2>Как работает учёный</h2>
<ol>
<li>Задаёт вопрос: «Почему так происходит?»</li>
<li>Выдвигает гипотезу — предполагаемый ответ.</li>
<li>Проводит опыт или наблюдение и собирает данные.</li>
<li>Проверяет, подтвердилась ли гипотеза, и делится результатами с другими.</li>
</ol>
<h2>Что изучают в Кыргызстане</h2>
<p>Тем для исследований очень много: ледники и реки, землетрясения, озеро Иссык-Куль, редкие животные вроде снежного барса, древние города на Великом шёлковом пути и эпос «Манас». В стране работают Национальная академия наук и много университетов.</p>
<h2>Что пригодится</h2>
<p>Любопытство, терпение, аккуратность и смелость ошибаться: даже неудачный опыт чему-то учит.</p>
<h2>С чего начать</h2>
<p>Веди дневник наблюдений за природой, участвуй в школьных научных проектах и олимпиадах, записывай свои интересные вопросы.</p>''',
         '''<p>A <strong>scientist</strong> is someone who studies how the world works. Scientists ask questions, observe, run experiments and check their answers with evidence.</p>
<h2>How a scientist works</h2>
<ol>
<li>Asks a question: “Why does this happen?”</li>
<li>Makes a hypothesis — a possible answer.</li>
<li>Runs an experiment or makes observations and collects data.</li>
<li>Checks whether the hypothesis was right and shares the results with others.</li>
</ol>
<h2>What is studied in Kyrgyzstan</h2>
<p>There is a lot to explore: glaciers and rivers, earthquakes, Lake Issyk-Kul, rare animals such as the snow leopard, ancient towns on the Great Silk Road and the Manas epic. The country has a National Academy of Sciences and many universities.</p>
<h2>What helps</h2>
<p>Curiosity, patience, accuracy and not being afraid of mistakes: even a failed experiment teaches you something.</p>
<h2>Where to start</h2>
<p>Keep a nature observation diary, take part in school science projects and olympiads, and write down your interesting questions.</p>''',
     ),
     'facts': []},

    {'slug': 'designer', 'category': ('modern', 'professions'), 'layout': 'profession',
     'title': ('Дизайнер', 'Дизайнер', 'Designer'),
     'summary': (
         'Дизайнер нерселерди кооз жана ыңгайлуу кылат — логотиптен тартып кийимге чейин.',
         'Дизайнер делает вещи красивыми и удобными — от логотипа до одежды.',
         'A designer makes things beautiful and easy to use — from logos to clothes.',
     ),
     'body': (
         '''<p><strong>Дизайнер</strong> нерселер кандай көрүнөрүн жана аларды колдонуу канчалык ыңгайлуу болоорун ойлоп табат. Китептин мукабасы, телефондогу тиркеме, кийим, бөлмөнүн ичи — мунун баарын дизайнерлер жасашат.</p>
<h2>Кандай дизайнерлер болот?</h2>
<ul>
<li><strong>графикалык дизайнер</strong> логотиптерди, плакаттарды жана китептерди жасайт;</li>
<li><strong>интерфейс дизайнери</strong> сайттарды жана тиркемелерди ыңгайлуу кылат;</li>
<li><strong>кийим дизайнери</strong> кийимдин жаңы моделдерин ойлоп табат;</li>
<li><strong>интерьер дизайнери</strong> бөлмөлөрдү жасалгалайт.</li>
</ul>
<h2>Салт менен азыркы заман</h2>
<p>Кыргызстандын көп дизайнерлери улуттук маданияттан шыктанышат: азыркы кийимге, буюмдарга жана сайттарга кочкор мүйүз сыяктуу оюм-чийимдерди, шырдактын түстөрүн, түндүктүн формасын кошушат. Ошентип эски салт жаңыча жашай баштайт.</p>
<h2>Эмне керек болот?</h2>
<p>Сүрөт тартуу, түстөрдү жана формаларды сезүү, графикалык программаларды билүү, ошондой эле адамдарды угуу жөндөмү: дизайн ал үчүн жасалат.</p>
<h2>Эмнеден баштаса болот?</h2>
<p>Көп тарт, айланаңдагы буюмдар кантип жасалганына көңүл бур жана акысыз графикалык редактордо открытка же плакат жасап көр.</p>''',
         '''<p><strong>Дизайнер</strong> придумывает, как вещи будут выглядеть и насколько удобно ими будет пользоваться. Обложка книги, приложение в телефоне, одежда, интерьер комнаты — всё это работа дизайнеров.</p>
<h2>Какие бывают дизайнеры</h2>
<ul>
<li><strong>графический дизайнер</strong> делает логотипы, плакаты и книги;</li>
<li><strong>дизайнер интерфейсов</strong> делает сайты и приложения удобными;</li>
<li><strong>дизайнер одежды</strong> придумывает новые модели одежды;</li>
<li><strong>дизайнер интерьеров</strong> оформляет помещения.</li>
</ul>
<h2>Традиции и современность</h2>
<p>Многие дизайнеры в Кыргызстане вдохновляются национальной культурой: добавляют в современную одежду, вещи и сайты орнаменты вроде «кочкор мүйүз», цвета шырдака, форму тюндюка. Так старые традиции получают новую жизнь.</p>
<h2>Что пригодится</h2>
<p>Рисование, чувство цвета и формы, умение работать в графических программах и умение слушать людей: ведь дизайн делают для них.</p>
<h2>С чего начать</h2>
<p>Больше рисуй, обращай внимание на то, как сделаны вещи вокруг тебя, и попробуй сделать открытку или плакат в бесплатном графическом редакторе.</p>''',
         '''<p>A <strong>designer</strong> decides how things will look and how easy they will be to use. A book cover, a phone app, clothes, the inside of a room — all of these are made by designers.</p>
<h2>Kinds of designers</h2>
<ul>
<li>a <strong>graphic designer</strong> creates logos, posters and books;</li>
<li>an <strong>interface designer</strong> makes websites and apps easy to use;</li>
<li>a <strong>fashion designer</strong> creates new clothes;</li>
<li>an <strong>interior designer</strong> decorates rooms and spaces.</li>
</ul>
<h2>Tradition meets today</h2>
<p>Many designers in Kyrgyzstan are inspired by national culture: they add ornaments such as “kochkor muyuz”, the colours of the shyrdak or the shape of the tunduk to modern clothes, objects and websites. That way old traditions get a new life.</p>
<h2>What helps</h2>
<p>Drawing, a feel for colour and shape, knowing how to use graphics software and being able to listen to people — after all, design is made for them.</p>
<h2>Where to start</h2>
<p>Draw a lot, notice how the things around you are made, and try making a card or a poster in a free graphics editor.</p>''',
     ),
     'facts': []},
]


QUIZZES = [
    {'slug': 'nature-and-animals', 'topic': 'nature', 'difficulty': 'easy',
     'title': ('Жаратылыш жана жаныбарлар', 'Природа и животные', 'Nature and animals'),
     'summary': (
         'Кыргызстандын тоолору, көлдөрү жана жаныбарлары жөнүндө эмне билесиң?',
         'Что ты знаешь о горах, озёрах и животных Кыргызстана?',
         'What do you know about the mountains, lakes and animals of Kyrgyzstan?',
     ),
     'questions': [
        {'text': ('Бишкектин гербинде кайсы жаныбар сүрөттөлгөн?', 'Какое животное изображено на гербе Бишкека?', 'Which animal is shown on the coat of arms of Bishkek?'),
         'explanation': ('Илбирс — Бишкектин символу жана сейрек кездешүүчү тоо жаныбары.', 'Снежный барс — символ Бишкека и редкий горный зверь.', 'The snow leopard is a symbol of Bishkek and a rare mountain animal.'),
         'home': True,
         'answers': [
             (('Илбирс', 'Снежный барс', 'Snow leopard'), True),
             (('Аюу', 'Медведь', 'Bear'), False),
             (('Карышкыр', 'Волк', 'Wolf'), False),
             (('Түлкү', 'Лиса', 'Fox'), False),
         ]},
        {'text': ('Кыргызстандагы эң чоң көл кайсы?', 'Какое озеро самое большое в Кыргызстане?', 'What is the largest lake in Kyrgyzstan?'),
         'explanation': ('Ысык-Көл — өлкөнүн эң чоң көлү, ал кышында да тоңбойт.', 'Иссык-Куль — самое большое озеро страны, и зимой оно не замерзает.', 'Issyk-Kul is the largest lake in the country, and it does not freeze in winter.'),
         'home': False,
         'answers': [
             (('Ысык-Көл', 'Иссык-Куль', 'Issyk-Kul'), True),
             (('Соң-Көл', 'Сон-Куль', 'Son-Kul'), False),
             (('Чатыр-Көл', 'Чатыр-Куль', 'Chatyr-Kul'), False),
             (('Сары-Челек', 'Сары-Челек', 'Sary-Chelek'), False),
         ]},
        {'text': ('Кыргызстандын көпчүлүк бөлүгүн кайсы тоо системасы ээлейт?', 'Какая горная система занимает большую часть Кыргызстана?', 'Which mountain system covers most of Kyrgyzstan?'),
         'explanation': ('Теңир-Тоо (Тянь-Шань) өлкөнүн көпчүлүк бөлүгүн ээлейт, түштүгүндө Памир-Алай жайгашкан.', 'Тянь-Шань (Теңир-Тоо) занимает большую часть страны, а на юге находится Памиро-Алай.', 'The Tian Shan (Teñir-Too) covers most of the country, and the Pamir-Alai is in the south.'),
         'home': False,
         'answers': [
             (('Теңир-Тоо (Тянь-Шань)', 'Тянь-Шань', 'The Tian Shan'), True),
             (('Альп тоолору', 'Альпы', 'The Alps'), False),
             (('Урал тоолору', 'Уральские горы', 'The Ural Mountains'), False),
             (('Анд тоолору', 'Анды', 'The Andes'), False),
         ]},
        {'text': ('Нарын сыяктуу тоо дарыялары суусун негизинен кайдан алат?', 'Откуда горные реки, такие как Нарын, получают больше всего воды?', 'Where do mountain rivers like the Naryn get most of their water?'),
         'explanation': ('Жайында мөңгүлөр жана тоодогу кар эрийт, ал эриген суу дарыяларды толтурат.', 'Летом тают ледники и снег в горах, и талая вода наполняет реки.', 'In summer, glaciers and mountain snow melt, and the meltwater fills the rivers.'),
         'home': False,
         'answers': [
             (('Эриген мөңгүлөрдөн жана кардан', 'От тающих ледников и снега', 'From melting glaciers and snow'), True),
             (('Деңизден', 'Из моря', 'From the sea'), False),
             (('Суу түтүктөрүнөн', 'Из водопровода', 'From water pipes'), False),
             (('Чөлдөн', 'Из пустыни', 'From the desert'), False),
         ]},
        {'text': ('Кыргызстандын эң бийик чокусу кайсы?', 'Какая вершина самая высокая в Кыргызстане?', 'What is the highest peak in Kyrgyzstan?'),
         'explanation': ('Жеңиш чокусунун бийиктиги — 7439 метр, ал Кытай менен чек арада жайгашкан.', 'Высота Жеңиш чокусу (пика Победы) — 7439 метров, он стоит на границе с Китаем.', 'Jengish Chokusu (Victory Peak) is 7,439 metres high and stands on the border with China.'),
         'home': False,
         'answers': [
             (('Жеңиш чокусу', 'Жеңиш чокусу (пик Победы)', 'Jengish Chokusu (Victory Peak)'), True),
             (('Эверест', 'Эверест', 'Everest'), False),
             (('Эльбрус', 'Эльбрус', 'Elbrus'), False),
             (('Монблан', 'Монблан', 'Mont Blanc'), False),
         ]},
     ]},

    {'slug': 'kyrgyz-words', 'topic': 'language', 'difficulty': 'easy',
     'title': ('Кыргыз сөздөрү', 'Кыргызские слова', 'Kyrgyz words'),
     'summary': (
         'Эң керектүү кыргыз сөздөрүн билесиңби? Текшерип көр!',
         'Знаешь ли ты самые нужные кыргызские слова? Проверь себя!',
         'Do you know the most useful Kyrgyz words? Test yourself!',
     ),
     'questions': [
        {'text': ('«Салам» сөзү орусчага кандай которулат?', 'Что означает кыргызское слово «Салам»?', 'What does the Kyrgyz word “Salam” mean?'),
         'explanation': ('«Салам» — жолукканда айтылуучу учурашуу сөзү.', '«Салам» — так здороваются при встрече.', '“Salam” is what you say to greet someone.'),
         'home': True,
         'answers': [
             (('Привет', 'Привет', 'Hello'), True),
             (('Пока', 'Пока', 'Goodbye'), False),
             (('Спасибо', 'Спасибо', 'Thank you'), False),
             (('Да', 'Да', 'Yes'), False),
         ]},
        {'text': ('«Рахмат» сөзү орусчага кандай которулат?', 'Что означает слово «Рахмат»?', 'What does “Rakhmat” mean?'),
         'explanation': ('«Рахмат» деп ыраазычылык билдиришет.', '«Рахмат» говорят, когда благодарят.', 'People say “Rakhmat” to thank someone.'),
         'home': False,
         'answers': [
             (('Спасибо', 'Спасибо', 'Thank you'), True),
             (('Извините', 'Извините', 'Sorry'), False),
             (('Нет', 'Нет', 'No'), False),
             (('Доброе утро', 'Доброе утро', 'Good morning'), False),
         ]},
        {'text': ('«Тоо» сөзү орусчага кандай которулат?', 'Что означает слово «Тоо»?', 'What does “Too” mean?'),
         'explanation': ('«Тоо» — гора. Мисалы, Теңир-Тоо, Ала-Тоо.', '«Тоо» — гора. Например, Теңир-Тоо, Ала-Тоо.', '“Too” means mountain — as in Teñir-Too or Ala-Too.'),
         'home': False,
         'answers': [
             (('Гора', 'Гора', 'Mountain'), True),
             (('Река', 'Река', 'River'), False),
             (('Дом', 'Дом', 'House'), False),
             (('Дерево', 'Дерево', 'Tree'), False),
         ]},
        {'text': ('«Көл» сөзү орусчага кандай которулат?', 'Что означает слово «Көл»?', 'What does “Köl” mean?'),
         'explanation': ('«Көл» — озеро. Ысык-Көл, Соң-Көл деген аталыштарда ушул сөз бар.', '«Көл» — озеро. Это слово есть в названиях Иссык-Куль и Сон-Куль.', '“Köl” means lake. You can hear it in the names Issyk-Kul and Son-Kul.'),
         'home': False,
         'answers': [
             (('Озеро', 'Озеро', 'Lake'), True),
             (('Поле', 'Поле', 'Field'), False),
             (('Ветер', 'Ветер', 'Wind'), False),
             (('Снег', 'Снег', 'Snow'), False),
         ]},
        {'text': ('Кыргызча «5» кандай айтылат?', 'Как по-кыргызски будет число «5»?', 'How do you say the number 5 in Kyrgyz?'),
         'explanation': ('Бир, эки, үч, төрт, беш — беш = 5.', 'Бир, эки, үч, төрт, беш — «беш» значит 5.', 'Bir, eki, üch, tört, besh — “besh” means 5.'),
         'home': False,
         'answers': [
             (('Беш', 'Беш', 'Besh'), True),
             (('Үч', 'Үч', 'Üch'), False),
             (('Жети', 'Жети', 'Zheti'), False),
             (('Он', 'Он', 'On'), False),
         ]},
     ]},

    {'slug': 'history-of-kyrgyzstan', 'topic': 'history', 'difficulty': 'medium',
     'title': ('Кыргызстандын тарыхы', 'История Кыргызстана', 'History of Kyrgyzstan'),
     'summary': (
         'Борбор шаар, эгемендүүлүк, желек жана Улуу Жибек жолу.',
         'Столица, независимость, флаг и Великий шёлковый путь.',
         'The capital, independence, the flag and the Great Silk Road.',
     ),
     'questions': [
        {'text': ('Кыргызстандын борбор шаары кайсы?', 'Какой город — столица Кыргызстана?', 'What is the capital of Kyrgyzstan?'),
         'explanation': ('Бишкек — Кыргызстандын борбору жана эң чоң шаары.', 'Бишкек — столица и самый большой город Кыргызстана.', 'Bishkek is the capital and the largest city of Kyrgyzstan.'),
         'home': True,
         'answers': [
             (('Бишкек', 'Бишкек', 'Bishkek'), True),
             (('Ош', 'Ош', 'Osh'), False),
             (('Каракол', 'Каракол', 'Karakol'), False),
             (('Талас', 'Талас', 'Talas'), False),
         ]},
        {'text': ('Кыргызстан эгемендүүлүгүн качан жарыялаган?', 'Когда Кыргызстан провозгласил независимость?', 'When did Kyrgyzstan declare independence?'),
         'explanation': ('1991-жылдын 31-августунда Кыргызстан эгемендүү мамлекет болуп жарыяланган. Бул күн — Эгемендүүлүк күнү.', '31 августа 1991 года Кыргызстан провозгласил независимость. Этот день — День независимости.', 'Kyrgyzstan declared independence on 31 August 1991. This day is Independence Day.'),
         'home': False,
         'answers': [
             (('1991-жылдын 31-августу', '31 августа 1991 года', '31 August 1991'), True),
             (('1990-жылдын 1-январы', '1 января 1990 года', '1 January 1990'), False),
             (('1995-жылдын 21-марты', '21 марта 1995 года', '21 March 1995'), False),
             (('2000-жылдын 5-марты', '5 марта 2000 года', '5 March 2000'), False),
         ]},
        {'text': ('Кыргызстандын желегиндеги күндүн канча нуру бар?', 'Сколько лучей у солнца на флаге Кыргызстана?', 'How many rays does the sun on the flag of Kyrgyzstan have?'),
         'explanation': ('Кызыл желектеги сары күндүн 40 нуру бар — алар 40 кыргыз уруусун билдирет. Күндүн ортосунда түндүк сүрөттөлгөн.', 'У жёлтого солнца на красном флаге 40 лучей — они символизируют 40 кыргызских племён. В центре солнца изображён тюндюк.', 'The yellow sun on the red flag has 40 rays, which stand for the 40 Kyrgyz tribes. A tunduk is shown in the centre of the sun.'),
         'home': False,
         'answers': [
             (('40', '40', '40'), True),
             (('12', '12', '12'), False),
             (('7', '7', '7'), False),
             (('100', '100', '100'), False),
         ]},
        {'text': ('Токмоктун жанындагы Бурана мунарасы деген эмне?', 'Что такое башня Бурана возле Токмока?', 'What is the Burana Tower near Tokmok?'),
         'explanation': ('Бурана — орто кылымдарда курулган мунара (минарет). Анын жанында байыркы шаардын калдыктары табылган.', 'Бурана — средневековый минарет. Рядом с ним находятся остатки древнего города.', 'Burana is a medieval minaret. The remains of an ancient town lie around it.'),
         'home': False,
         'answers': [
             (('Орто кылымдагы мунара (минарет)', 'Средневековый минарет', 'A medieval minaret'), True),
             (('Азыркы телемунара', 'Современная телебашня', 'A modern TV tower'), False),
             (('Маяк', 'Маяк', 'A lighthouse'), False),
             (('Суу мунарасы', 'Водонапорная башня', 'A water tower'), False),
         ]},
        {'text': ('Байыркы убакта Кыргызстандын аймагы аркылуу кайсы соода жолу өткөн?', 'Какой древний торговый путь проходил через территорию Кыргызстана?', 'Which ancient trade route passed through the territory of Kyrgyzstan?'),
         'explanation': ('Улуу Жибек жолу Кытайды Батыш менен байланыштырган. Нарын облусундагы Таш-Рабат — соодагерлер токтогон таш кербен сарай.', 'Великий шёлковый путь связывал Китай с Западом. Таш-Рабат в Нарынской области — каменный караван-сарай, где останавливались торговцы.', 'The Great Silk Road linked China with the West. Tash-Rabat in Naryn Region is a stone caravanserai where traders stopped.'),
         'home': False,
         'answers': [
             (('Улуу Жибек жолу', 'Великий шёлковый путь', 'The Great Silk Road'), True),
             (('Транссибирь темир жолу', 'Транссибирская магистраль', 'The Trans-Siberian Railway'), False),
             (('Панама каналы', 'Панамский канал', 'The Panama Canal'), False),
             (('Римдин Аппий жолу', 'Аппиева дорога в Риме', 'The Appian Way in Rome'), False),
         ]},
     ]},
]


WORD_TOPICS = [
    {'slug': 'numbers',
     'title': ('Сандар', 'Числа', 'Numbers'),
     'summary': ('Бирден онго чейин санайбыз.', 'Учимся считать по-кыргызски от одного до десяти.', 'Learn to count from one to ten in Kyrgyz.'),
     'words': [
         ('Бир', 'bir', 'Один', 'One'),
         ('Эки', 'eki', 'Два', 'Two'),
         ('Үч', 'üch', 'Три', 'Three'),
         ('Төрт', 'tört', 'Четыре', 'Four'),
         ('Беш', 'besh', 'Пять', 'Five'),
         ('Алты', 'alty', 'Шесть', 'Six'),
         ('Жети', 'zheti', 'Семь', 'Seven'),
         ('Сегиз', 'segiz', 'Восемь', 'Eight'),
         ('Тогуз', 'toguz', 'Девять', 'Nine'),
         ('Он', 'on', 'Десять', 'Ten'),
     ]},
    {'slug': 'colors',
     'title': ('Түстөр', 'Цвета', 'Colours'),
     'summary': ('Ак, кара, кызыл жана башка түстөр.', 'Белый, чёрный, красный — как называются цвета по-кыргызски.', 'White, black, red — the names of colours in Kyrgyz.'),
     'words': [
         ('Ак', 'ak', 'Белый', 'White'),
         ('Кара', 'kara', 'Чёрный', 'Black'),
         ('Кызыл', 'kyzyl', 'Красный', 'Red'),
         ('Сары', 'sary', 'Жёлтый', 'Yellow'),
         ('Көк', 'kök', 'Синий', 'Blue'),
         ('Жашыл', 'zhashyl', 'Зелёный', 'Green'),
         ('Боз', 'boz', 'Серый', 'Grey'),
         ('Күрөң', 'küröng', 'Коричневый', 'Brown'),
     ]},
    {'slug': 'animals',
     'title': ('Жаныбарлар', 'Животные', 'Animals'),
     'summary': ('Үй жаныбарлары жана тоо жаныбарлары.', 'Домашние животные и жители гор — как они называются по-кыргызски.', 'Farm animals, pets and mountain animals in Kyrgyz.'),
     'words': [
         ('Ат', 'at', 'Лошадь', 'Horse'),
         ('Кой', 'koy', 'Овца', 'Sheep'),
         ('Уй', 'uy', 'Корова', 'Cow'),
         ('Төө', 'töö', 'Верблюд', 'Camel'),
         ('Эчки', 'echki', 'Коза', 'Goat'),
         ('Ит', 'it', 'Собака', 'Dog'),
         ('Мышык', 'myshyk', 'Кошка', 'Cat'),
         ('Бүркүт', 'bürküt', 'Беркут', 'Golden eagle'),
         ('Илбирс', 'ilbirs', 'Снежный барс', 'Snow leopard'),
     ]},
]


PUZZLES = [
    {'topic': 'nature',
     'ky': {'prompt': 'Бийик тоодо жашаймын,\nкуйругум узун, жүнүм калың,\nтактуу тонум карда билинбейт.\nМен киммин?',
            'answer': 'Илбирс', 'alt': 'ирбис\nкар илбирси',
            'hint': 'Ал Бишкектин гербинде бар.',
            'explanation': 'Илбирс — сейрек кездешүүчү тоо мышыгы, Кызыл китепке киргизилген.'},
     'ru': {'prompt': 'Живу высоко в горах,\nхвост длинный, шуба густая,\nпятнистую шубку в снегу не видно.\nКто я?',
            'answer': 'Снежный барс', 'alt': 'барс\nирбис\nилбирс\nснежный леопард',
            'hint': 'Он изображён на гербе Бишкека.',
            'explanation': 'Снежный барс (илбирс) — редкая горная кошка, занесённая в Красную книгу.'},
     'en': {'prompt': 'I live high in the mountains,\nmy tail is long, my fur is thick,\nmy spotted coat hides in the snow.\nWho am I?',
            'answer': 'Snow leopard', 'alt': 'irbis\nilbirs\nounce',
            'hint': 'It is on the coat of arms of Bishkek.',
            'explanation': 'The snow leopard (ilbirs) is a rare mountain cat listed in the Red Book.'}},

    {'topic': 'geography',
     'ky': {'prompt': 'Тоодо жатат кылымдар бою,\nжайында эрийт акырын,\nдарыяларга суу берет.\nБул эмне?',
            'answer': 'Мөңгү', 'alt': 'мөнгү\nмонгу',
            'hint': 'Бул — тоодогу чоң муз.',
            'explanation': 'Мөңгүлөр жайында эрип, Нарын сыяктуу дарыяларды суу менен толтурат.'},
     'ru': {'prompt': 'Веками лежит в горах,\nлетом понемногу тает,\nреки водой наполняет.\nЧто это?',
            'answer': 'Ледник', 'alt': 'мөңгү\nглетчер',
            'hint': 'Это огромная масса льда в горах.',
            'explanation': 'Ледники тают летом и питают реки, например Нарын.'},
     'en': {'prompt': 'For centuries I lie in the mountains,\nin summer I slowly melt,\nand I fill the rivers with water.\nWhat am I?',
            'answer': 'Glacier', 'alt': 'a glacier\nmöngü\nmongu',
            'hint': 'It is a huge mass of ice in the mountains.',
            'explanation': 'Glaciers melt in summer and feed rivers such as the Naryn.'}},

    {'topic': 'culture',
     'ky': {'prompt': 'Мени жайып салышат,\nүстүмө нан, чай коюшат,\nконокторду мен менен сыйлашат.\nМен эмнемин?',
            'answer': 'Дасторкон', 'alt': 'дастаркон\nдастархан',
            'hint': 'Конок келгенде аны жайышат.',
            'explanation': 'Дасторкон — конокко жайылган сый, ага нан, боорсок, чай жана тамак коюлат.'},
     'ru': {'prompt': 'Меня расстилают,\nхлеб и чай на меня ставят,\nгостей угощают.\nЧто я?',
            'answer': 'Дастархан', 'alt': 'дасторкон\nдастаркон',
            'hint': 'Его расстилают, когда приходят гости.',
            'explanation': 'Дастархан (дасторкон) — скатерть с угощением: хлеб, боорсоки, чай и другие блюда.'},
     'en': {'prompt': 'People spread me out,\nput bread and tea on me\nand treat their guests.\nWhat am I?',
            'answer': 'Dastorkon', 'alt': 'dastarkhan\ndastarkon\ndasturkon',
            'hint': 'It is spread out when guests arrive.',
            'explanation': 'A dastorkon is a cloth laid with food for guests: bread, boorsok, tea and other dishes.'}},

    {'topic': 'culture',
     'ky': {'prompt': 'Тактада эки катар уя,\nар бир оюнчуда тогуздан,\nар уяда тогуз коргоол.\nБул кайсы оюн?',
            'answer': 'Тогуз коргоол', 'alt': 'тогуз коргол\nтогузкоргоол\nтогуз-коргоол',
            'hint': 'Аталышында «тогуз» деген сан бар.',
            'explanation': 'Тогуз коргоол — эки кишилик акыл оюну. Ар бир оюнчуда 9 уя, ар бир уяда башында 9 коргоол болот.'},
     'ru': {'prompt': 'На доске два ряда лунок,\nу каждого игрока их девять,\nв каждой лунке — девять камешков.\nЧто это за игра?',
            'answer': 'Тогуз коргоол', 'alt': 'тогуз коргол\nтогузкоргоол\nтогуз-коргоол\nтогуз кумалак',
            'hint': 'В её названии есть число «девять».',
            'explanation': 'Тогуз коргоол — логическая игра для двоих. У каждого игрока 9 лунок, и в начале в каждой лежит по 9 камешков-коргоолов.'},
     'en': {'prompt': 'A board with two rows of holes,\nnine holes for each player,\nnine little stones in each.\nWhat game is this?',
            'answer': 'Toguz korgool', 'alt': 'togyz kumalak\ntoguz-korgool\ntoguzkorgool\ntoguz korgol',
            'hint': 'Its name contains the number nine.',
            'explanation': 'Toguz korgool is a strategy game for two. Each player has 9 holes, and each hole starts with 9 stones called korgools.'}},

    {'topic': 'nature',
     'ky': {'prompt': 'Канаттарым кең, көзүм курч,\nбийиктен баарын көрөм,\nбүркүтчү менен аңга чыгам.\nМен киммин?',
            'answer': 'Бүркүт', 'alt': 'буркут',
            'hint': 'Аны колго үйрөткөн мергенди бүркүтчү деп аташат.',
            'explanation': 'Бүркүт — чоң, күчтүү жырткыч куш. Кыргыздарда бүркүт менен аңчылык кылуу салты бар.'},
     'ru': {'prompt': 'Крылья широкие, глаз зоркий,\nс высоты всё вижу,\nс охотником-беркутчи на охоту летаю.\nКто я?',
            'answer': 'Беркут', 'alt': 'бүркүт\nбуркут\nорёл\nорел',
            'hint': 'Охотника, который его приручил, называют бүркүтчү.',
            'explanation': 'Беркут — крупная сильная хищная птица. У кыргызов есть традиция охоты с беркутом.'},
     'en': {'prompt': 'My wings are wide, my eyes are sharp,\nI see everything from high above,\nI hunt together with a burkutchu.\nWho am I?',
            'answer': 'Golden eagle', 'alt': 'eagle\nberkut\nburkut\nbürküt',
            'hint': 'The hunter who trains it is called a burkutchu.',
            'explanation': 'The golden eagle is a large, strong bird of prey. The Kyrgyz have a tradition of hunting with golden eagles.'}},

    {'topic': 'language',
     'ky': {'prompt': 'Үч эле тамгадан турам,\nКыргызстанда мен абдан көпмүн,\nчокумда кар жатат.\nМен кайсы сөзмүн?',
            'answer': 'Тоо', 'alt': 'тоолор',
            'hint': 'Теңир-Тоо, Ала-Тоо...',
            'explanation': '«Тоо» — тоо. Тоолор Кыргызстандын көпчүлүк бөлүгүн ээлейт.'},
     'ru': {'prompt': 'Кыргызское слово из трёх букв.\nВ Кыргызстане меня очень много,\nна моей вершине лежит снег.\nКакое это слово?',
            'answer': 'Тоо', 'alt': 'too',
            'hint': 'Теңир-Тоо, Ала-Тоо...',
            'explanation': '«Тоо» по-кыргызски значит «гора». Горы занимают большую часть Кыргызстана.'},
     'en': {'prompt': 'A Kyrgyz word of three letters.\nThere are lots of me in Kyrgyzstan,\nand snow lies on my top.\nWhat is the word?',
            'answer': 'Too', 'alt': 'тоо',
            'hint': 'Teñir-Too, Ala-Too...',
            'explanation': '“Too” is Kyrgyz for “mountain”. Mountains cover most of Kyrgyzstan.'}},
]
