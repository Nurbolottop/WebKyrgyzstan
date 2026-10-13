"""Описания областей и достопримечательностей (для команды seed_more). Кортежи — (ky, ru, en)."""

REGIONS = {
    'chuy': {
        'summary': (
            'Чүй облусу — өлкөнүн түндүгүндөгү кенен, түшүмдүү өрөөн. Ал борбор шаар Бишкекти курчап турат.',
            'Чуйская область — широкая плодородная долина на севере страны. Она окружает столицу — Бишкек.',
            'Chuy Region is a wide, fertile valley in the north of the country. It surrounds the capital, Bishkek.',
        ),
        'body': (
            '''<p>Чүй облусу Кыргызстандын түндүгүндө жайгашкан. Бул жерде өлкөнүн эң көп калктуу аймактарынын бири жана борбор шаар Бишкек бар.</p>
<p>Түздүктөрдө талаалар, бактар жана айылдар жайылып жатат, ал эми түштүгүндө Кыргыз Ала-Тоосунун кар баскан чокулары көрүнүп турат.</p>''',
            '''<p>Чуйская область находится на севере Кыргызстана. Здесь живёт очень много людей, а в самом её центре расположена столица — Бишкек.</p>
<p>На равнинах раскинулись поля, сады и сёла, а на юге видны снежные вершины Кыргызского Ала-Тоо. Представь: летом жарко в долине, а в горах в это время лежит снег!</p>''',
            '''<p>Chuy Region lies in the north of Kyrgyzstan. It is one of the most populated parts of the country, and the capital, Bishkek, sits right in the middle of it.</p>
<p>Fields, orchards and villages spread across the plains, while the snowy peaks of the Kyrgyz Ala-Too range rise to the south.</p>''',
        ),
        'geography': (
            '''<p>Облустун негизги бөлүгүн Чүй өрөөнү түзөт. Өрөөн аркылуу Чүй дарыясы агат, анын бир бөлүгү Кыргызстан менен Казакстандын ортосундагы чек ара болуп саналат.</p>
<p>Түштүгүндө Кыргыз Ала-Тоо кырка тоосу созулуп жатат. Түндүк тарабы жапыз жана жайык, ошондуктан бул жерде дыйканчылык жакшы өнүккөн.</p>''',
            '''<p>Главная часть области — Чуйская долина. По ней течёт река Чу, и на одном участке она служит границей между Кыргызстаном и Казахстаном.</p>
<p>С юга долину закрывает хребет Кыргызский Ала-Тоо. Север области ниже и ровнее, поэтому здесь удобно заниматься земледелием.</p>''',
            '''<p>The heart of the region is the Chuy Valley. The Chuy River flows through it, and along one stretch the river forms the border between Kyrgyzstan and Kazakhstan.</p>
<p>To the south stands the Kyrgyz Ala-Too mountain range. The northern part is lower and flatter, which makes it good for farming.</p>''',
        ),
        'nature': (
            '''<p>Бишкектин жанында Ала-Арча улуттук паркы жайгашкан. Анда арча токойлору, тоо суулары жана мөңгүлөр бар.</p>
<p>Чүй өрөөнүндөгү түшүмдүү жерлерде буудай, жүгөрү, жашылчалар жана мөмө-жемиштер өстүрүлөт. Тоолордун этегинде шаркыратмалары бар көптөгөн капчыгайлар бар.</p>''',
            '''<p>Рядом с Бишкеком находится национальный парк Ала-Арча с можжевеловыми лесами, горными реками и ледниками.</p>
<p>На плодородных землях Чуйской долины выращивают пшеницу, кукурузу, овощи и фрукты. А у подножия гор прячется множество ущелий с водопадами.</p>''',
            '''<p>Near Bishkek is Ala-Archa National Park, with juniper forests, mountain rivers and glaciers.</p>
<p>The fertile land of the Chuy Valley grows wheat, corn, vegetables and fruit. At the foot of the mountains there are many gorges with waterfalls.</p>''',
        ),
        'culture': (
            '''<p>Чүй өрөөнү аркылуу илгери Улуу Жибек жолунун тармактары өткөн. Токмоктун жанында орто кылымдагы Баласагын шаарынын калдыктары жана Бурана мунарасы сакталып калган.</p>
<p>Бүгүн бул жерде ар түрдүү элдердин өкүлдөрү чогуу жашайт, ошондуктан облустун майрамдары жана тамак-аштары абдан ар түрдүү.</p>''',
            '''<p>Когда-то через Чуйскую долину проходили пути Великого Шёлкового пути. Возле города Токмок сохранились остатки средневекового города Баласагун и знаменитая башня Бурана.</p>
<p>Сегодня здесь живут вместе люди многих национальностей, поэтому праздники и кухня области очень разнообразны.</p>''',
            '''<p>Long ago, branches of the Great Silk Road crossed the Chuy Valley. Near the town of Tokmok you can still see the remains of the medieval city of Balasagun and the famous Burana Tower.</p>
<p>Today people of many different nationalities live here together, so the region’s holidays and food are very varied.</p>''',
        ),
        'area_km2': 20200,
        'facts': [
            (
                'Бишкек Чүй өрөөнүндө жайгашкан, бирок ал өзүнчө шаар катары эсептелет жана облустун курамына кирбейт.',
                'Бишкек стоит в Чуйской долине, но считается отдельным городом и в состав области не входит.',
                'Bishkek stands in the Chuy Valley, but it is a separate city and is not part of the region.',
            ),
            (
                'Бурана мунарасы — Баласагын шаарынан калган эң белгилүү эстелик.',
                'Башня Бурана — самый известный памятник, оставшийся от города Баласагун.',
                'Burana Tower is the best-known monument left from the city of Balasagun.',
            ),
        ],
    },
    'talas': {
        'summary': (
            'Талас облусу — өлкөнүн түндүк-батышындагы тоолуу өрөөн. Ал «Манас» эпосу менен тыгыз байланышкан.',
            'Таласская область — горная долина на северо-западе страны, тесно связанная с эпосом «Манас».',
            'Talas Region is a mountain valley in the north-west of the country, closely linked to the Manas epic.',
        ),
        'body': (
            '''<p>Талас — Кыргызстандын эң кичинекей облустарынын бири, бирок анын тарыхы абдан бай. Элдин айтымында, баатыр Манастын мекени ушул өрөөн болгон.</p>
<p>Таластын жанында «Манас Ордо» комплекси жайгашкан. Ага «Манас» эпосун сүйгөн адамдар бүт өлкөдөн келишет.</p>''',
            '''<p>Талас — одна из самых маленьких областей Кыргызстана, но её история очень богата. По народным преданиям, именно эта долина была родиной богатыря Манаса.</p>
<p>Недалеко от города Талас находится комплекс «Манас Ордо». Сюда приезжают люди со всей страны, которые любят эпос «Манас».</p>''',
            '''<p>Talas is one of the smallest regions of Kyrgyzstan, but its history is very rich. According to folk tradition, this valley was the homeland of the hero Manas.</p>
<p>Near the town of Talas stands the Manas Ordo complex. People who love the Manas epic come here from all over the country.</p>''',
        ),
        'geography': (
            '''<p>Облус Талас өрөөнүндө жайгашкан. Түштүгүндө Талас Ала-Тоосу, түндүгүндө Кыргыз Ала-Тоосу турат.</p>
<p>Өрөөн аркылуу Талас дарыясы агып, андан ары Казакстанга өтөт. Облус Казакстан жана Өзбекстан менен чектешет.</p>''',
            '''<p>Область лежит в Таласской долине. С юга её окружает Таласский Ала-Тоо, а с севера — Кыргызский Ала-Тоо.</p>
<p>По долине течёт река Талас, которая дальше уходит в Казахстан. Область граничит с Казахстаном и Узбекистаном.</p>''',
            '''<p>The region lies in the Talas Valley, with the Talas Ala-Too range to the south and the Kyrgyz Ala-Too range to the north.</p>
<p>The Talas River runs through the valley and continues into Kazakhstan. The region borders Kazakhstan and Uzbekistan.</p>''',
        ),
        'nature': (
            '''<p>Талас өрөөнү тоолор менен курчалган, анда жайыттар, тоо суулары жана арча токойлору бар.</p>
<p>Бул жердин жери түшүмдүү. Талас өзүнүн буурчагы менен белгилүү: аны көп өстүрүшөт жана башка өлкөлөргө да сатышат.</p>''',
            '''<p>Таласская долина окружена горами, здесь много пастбищ, горных рек и можжевеловых лесов.</p>
<p>Земля здесь плодородная. Талас знаменит своей фасолью: её выращивают очень много и даже продают в другие страны.</p>''',
            '''<p>The Talas Valley is surrounded by mountains, with pastures, mountain streams and juniper forests.</p>
<p>The soil here is fertile. Talas is famous for its beans: farmers grow a lot of them and even sell them to other countries.</p>''',
        ),
        'culture': (
            '''<p>«Манас» — кыргыз элинин улуу эпосу. Ал миңдеген саптан турат жана муундан муунга оозеки айтылып келген. Аны айткан адамдарды манасчы деп аташат.</p>
<p>«Манас Ордо» комплексинде Манас күмбөзү деп аталган байыркы күмбөз жана эпоско арналган музей бар.</p>''',
            '''<p>«Манас» — великий эпос кыргызского народа. Он состоит из огромного количества строк и веками передавался из уст в уста. Людей, которые его исполняют, называют манасчы.</p>
<p>В комплексе «Манас Ордо» есть старинный мавзолей, который называют Кумбез Манаса, и музей, посвящённый эпосу.</p>''',
            '''<p>Manas is the great epic of the Kyrgyz people. It is enormously long and was passed down by word of mouth for centuries. The storytellers who perform it are called manaschy.</p>
<p>The Manas Ordo complex includes an old mausoleum known as the Kumbez of Manas and a museum about the epic.</p>''',
        ),
        'area_km2': 11400,
        'facts': [
            (
                '«Манас» эпосу дүйнөдөгү эң узун эпостордун бири болуп эсептелет.',
                'Эпос «Манас» считается одним из самых длинных эпосов в мире.',
                'The Manas epic is considered one of the longest epic poems in the world.',
            ),
            (
                'Талас буурчагы Кыргызстандан чет өлкөлөргө сатылган белгилүү азыктардын бири.',
                'Таласская фасоль — один из известных продуктов, которые Кыргызстан продаёт за рубеж.',
                'Talas beans are one of the well-known products that Kyrgyzstan sells abroad.',
            ),
        ],
    },
    'issyk-kul': {
        'summary': (
            'Ысык-Көл облусу — өлкөнүн чыгышындагы аймак. Анын жүрөгү — улуу тоо көлү Ысык-Көл.',
            'Иссык-Кульская область — край на востоке страны. Её сердце — огромное горное озеро Иссык-Куль.',
            'Issyk-Kul Region is in the east of the country. Its heart is the huge mountain lake Issyk-Kul.',
        ),
        'body': (
            '''<p>Ысык-Көл облусу — Кыргызстандын эң белгилүү жайлоо жана эс алуу жерлеринин бири. Жайында жээктерге бүт өлкөдөн жана чет өлкөлөрдөн көп адамдар келишет.</p>
<p>Облустун борбору — Каракол шаары. Анын айланасында кооз капчыгайлар, ысык булактар жана бийик тоолор бар.</p>''',
            '''<p>Иссык-Кульская область — одно из самых любимых мест отдыха в Кыргызстане. Летом на берега озера приезжают люди со всей страны и из-за рубежа.</p>
<p>Центр области — город Каракол. Вокруг него красивые ущелья, горячие источники и высокие горы.</p>''',
            '''<p>Issyk-Kul Region is one of the most popular holiday places in Kyrgyzstan. In summer, people from all over the country and abroad come to the lake shores.</p>
<p>The regional centre is the town of Karakol, surrounded by beautiful gorges, hot springs and high mountains.</p>''',
        ),
        'geography': (
            '''<p>Ысык-Көл көлү эки кырка тоонун ортосунда жатат: түндүгүндө Күнгөй Ала-Тоо, түштүгүндө Тескей Ала-Тоо.</p>
<p>Облустун чыгышында Теңир-Тоонун эң бийик чокулары бар. Ошол жерде Кыргызстандын эң бийик чокусу — Жеңиш чокусу жана атактуу Хан-Теңири чокусу жайгашкан.</p>''',
            '''<p>Озеро Иссык-Куль лежит между двумя хребтами: на севере — Кюнгёй Ала-Тоо («солнечный»), на юге — Терскей Ала-Тоо («теневой»).</p>
<p>На востоке области поднимаются самые высокие вершины Тянь-Шаня. Здесь находится высшая точка Кыргызстана — пик Жеңиш (Победа), а также знаменитый пик Хан-Тенгри.</p>''',
            '''<p>Lake Issyk-Kul lies between two mountain ranges: Kungey Ala-Too (the “sunny side”) to the north and Terskey Ala-Too (the “shady side”) to the south.</p>
<p>The east of the region has the highest peaks of the Tian Shan, including Jengish Chokusu (Victory Peak), the highest point in Kyrgyzstan, and the famous Khan Tengri.</p>''',
        ),
        'nature': (
            '''<p>Каракол шаарынын жанында Жети-Өгүз капчыгайы бар. Анын кызыл аскалары жети өгүзгө окшош деп айтылат, ал эми бир аскасы «Сынган жүрөк» деп аталат.</p>
<p>Тескей Ала-Тоонун капчыгайларында карагай токойлору, шаркыратмалар жана ысык булактар көп. Тоолордо илбирс, тоо теке жана аркар сыяктуу жаныбарлар жашайт.</p>''',
            '''<p>Недалеко от Каракола находится ущелье Джети-Огуз. Его красные скалы, как говорят, похожи на семь быков, а одну скалу называют «Разбитое сердце».</p>
<p>В ущельях Терскей Ала-Тоо растут еловые леса, шумят водопады и бьют горячие источники. В горах живут снежный барс, горный козёл и архар.</p>''',
            '''<p>Near Karakol is Jeti-Oguz Gorge. Its red cliffs are said to look like seven bulls, and one rock is called the “Broken Heart”.</p>
<p>The gorges of Terskey Ala-Too have spruce forests, waterfalls and hot springs. Snow leopards, ibex and argali live in the mountains.</p>''',
        ),
        'culture': (
            '''<p>Каракол шаарына жакын жерде орус саякатчысы жана изилдөөчүсү Николай Пржевальскийдин мүрзөсү жана ага арналган музей бар.</p>
<p>Чолпон-Атада ачык асман алдындагы музей бар: анда миңдеген жылдар мурун ташка тартылган сүрөттөр — петроглифтер сакталган. Караколдо дунган мечити жана жыгач чиркөө да белгилүү.</p>''',
            '''<p>Рядом с Караколом находятся могила и музей русского путешественника и исследователя Николая Пржевальского.</p>
<p>В Чолпон-Ате есть музей под открытым небом: там сохранились петроглифы — рисунки на камнях, сделанные много веков назад. А в Караколе известны дунганская мечеть и деревянная церковь.</p>''',
            '''<p>Near Karakol are the grave and museum of the Russian traveller and explorer Nikolai Przhevalsky.</p>
<p>Cholpon-Ata has an open-air museum of petroglyphs — pictures carved on stones many centuries ago. Karakol is also known for its Dungan mosque and its wooden church.</p>''',
        ),
        'area_km2': 43100,
        'facts': [
            (
                'Ысык-Көл кышында да тоңбойт. Ошондуктан анын аты «ысык көл» дегенди билдирет.',
                'Иссык-Куль не замерзает даже зимой. Поэтому его название означает «горячее озеро».',
                'Issyk-Kul does not freeze even in winter, which is why its name means “warm (hot) lake”.',
            ),
            (
                'Кыргызстандын эң бийик чокусу — Жеңиш чокусу — Ысык-Көл облусунда, Кытай менен чек арада жайгашкан.',
                'Самая высокая вершина Кыргызстана — пик Жеңиш (Победа) — находится в Иссык-Кульской области на границе с Китаем.',
                'The highest peak of Kyrgyzstan, Jengish Chokusu (Victory Peak), is in Issyk-Kul Region on the border with China.',
            ),
            (
                'Караколдун жанындагы Жети-Өгүз аскалары кызыл түстө, анткени алардын тектерин темир кошулмалары боёп турат.',
                'Скалы Джети-Огуз красные потому, что их породу окрашивают соединения железа.',
                'The Jeti-Oguz cliffs are red because iron compounds colour the rock.',
            ),
        ],
    },
    'naryn': {
        'summary': (
            'Нарын облусу — Кыргызстандын эң тоолуу жана эң чоң облусу. Бул жерде бийик жайлоолор жана таза көлдөр көп.',
            'Нарынская область — самая гористая и самая большая область Кыргызстана с высокогорными пастбищами и чистыми озёрами.',
            'Naryn Region is the most mountainous and the largest region of Kyrgyzstan, full of high pastures and clear lakes.',
        ),
        'body': (
            '''<p>Нарын облусу өлкөнүн ортосунда жана түштүк-чыгышында жайгашкан. Анын дээрлик бардык жери бийик тоолордо жатат.</p>
<p>Бул жерде көп адамдар мал чарбачылыгы менен алектенишет. Жайында үй-бүлөлөр малын бийик жайлоолорго айдап чыгып, боз үйлөрдө жашашат.</p>''',
            '''<p>Нарынская область лежит в центре и на юго-востоке страны. Почти вся её территория находится высоко в горах.</p>
<p>Многие люди здесь занимаются животноводством. Летом семьи перегоняют скот на высокогорные пастбища — жайлоо — и живут в юртах. Хотел бы ты провести лето в юрте?</p>''',
            '''<p>Naryn Region lies in the centre and south-east of the country. Almost all of it is high in the mountains.</p>
<p>Many people here raise livestock. In summer, families take their animals up to high pastures called jailoo and live in yurts.</p>''',
        ),
        'geography': (
            '''<p>Облус аркылуу Нарын дарыясы агат. Ал Кыргызстандын эң узун дарыясы. Фергана өрөөнүндө Нарын Кара-Дарыя менен кошулуп, Сыр-Дарыяны түзөт.</p>
<p>Облустун түштүгүндө Кытай менен чек ара өтөт. Бул жерде Торугарт ашуусу жана бийик тоолуу Чатыр-Көл көлү бар.</p>''',
            '''<p>Через область течёт река Нарын — самая длинная река Кыргызстана. В Ферганской долине Нарын сливается с Карадарьёй, и вместе они образуют Сырдарью.</p>
<p>На юге область граничит с Китаем. Здесь находятся перевал Торугарт и высокогорное озеро Чатыр-Куль.</p>''',
            '''<p>The Naryn River flows through the region. It is the longest river in Kyrgyzstan. In the Fergana Valley it joins the Kara-Darya, and together they form the Syr Darya.</p>
<p>To the south the region borders China. Here you find the Torugart Pass and the high mountain lake Chatyr-Kul.</p>''',
        ),
        'nature': (
            '''<p>Нарын облусунда Соң-Көл көлү жайгашкан. Ал бийик тоолуу кооз көл, анын айланасы кенен жайлоолор менен курчалган.</p>
<p>Бул жерде кыш суук жана узун, ал эми жай салкын. Тоолордо топоз, тоо теке жана аркар жашайт.</p>''',
            '''<p>В Нарынской области находится озеро Сон-Куль — красивое высокогорное озеро, окружённое широкими пастбищами.</p>
<p>Зима здесь холодная и долгая, а лето прохладное. В горах живут яки, горные козлы и архары.</p>''',
            '''<p>Naryn Region is home to Son-Kul, a beautiful high mountain lake surrounded by wide pastures.</p>
<p>Winters here are cold and long, and summers are cool. Yaks, ibex and argali live in the mountains.</p>''',
        ),
        'culture': (
            '''<p>Нарындын жайлоолорунда көчмөн турмуштун салттары жакшы сакталган: боз үй тигүү, кымыз жасоо, ат оюндары.</p>
<p>Ат-Башы районунда Улуу Жибек жолунун тармагында курулган Таш-Рабат таш кербен сарайы бар.</p>''',
            '''<p>На пастбищах Нарына хорошо сохранились традиции кочевой жизни: сборка юрты, приготовление кумыса, конные игры.</p>
<p>В Ат-Башинском районе стоит каменный караван-сарай Таш-Рабат, построенный на ответвлении Великого Шёлкового пути.</p>''',
            '''<p>On the pastures of Naryn, nomadic traditions are well preserved: putting up yurts, making kymyz (fermented mare’s milk) and playing horse games.</p>
<p>In At-Bashy district stands Tash-Rabat, a stone caravanserai built on a branch of the Great Silk Road.</p>''',
        ),
        'area_km2': 45200,
        'facts': [
            (
                'Нарын — Кыргызстандын эң узун дарыясы жана Сыр-Дарыянын башаттарынын бири.',
                'Нарын — самая длинная река Кыргызстана и один из истоков Сырдарьи.',
                'The Naryn is the longest river in Kyrgyzstan and one of the sources of the Syr Darya.',
            ),
            (
                'Нарын облусу аянты боюнча Кыргызстандын эң чоң облусу.',
                'Нарынская область — самая большая область Кыргызстана по площади.',
                'Naryn is the largest region of Kyrgyzstan by area.',
            ),
        ],
    },
    'jalal-abad': {
        'summary': (
            'Жалал-Абад облусу — жаңгак токойлору, тоо көлдөрү жана чоң суу сактагычтары бар түштүктөгү аймак.',
            'Джалал-Абадская область — южный край ореховых лесов, горных озёр и больших водохранилищ.',
            'Jalal-Abad Region is a southern land of walnut forests, mountain lakes and large reservoirs.',
        ),
        'body': (
            '''<p>Жалал-Абад облусу өлкөнүн батышында жана түштүк-батышында жайгашкан. Ал Фергана өрөөнүнүн чет жакасынан баштап бийик тоолорго чейин созулат.</p>
<p>Облус Арстанбаптын жаңгак токойлору, Сары-Челек коругу жана Токтогул суу сактагычы менен белгилүү.</p>''',
            '''<p>Джалал-Абадская область находится на западе и юго-западе страны. Она тянется от края Ферганской долины до высоких гор.</p>
<p>Область знаменита ореховыми лесами Арсланбоба, заповедником Сары-Челек и Токтогульским водохранилищем.</p>''',
            '''<p>Jalal-Abad Region is in the west and south-west of the country. It stretches from the edge of the Fergana Valley up into high mountains.</p>
<p>The region is famous for the walnut forests of Arslanbob, the Sary-Chelek Reserve and the Toktogul Reservoir.</p>''',
        ),
        'geography': (
            '''<p>Облустун түндүгүндө Чаткал жана Талас Ала-Тоосу, чыгышында Фергана кырка тоосу бар. Ал эми түштүгүндө Фергана өрөөнүнүн жылуу түздүктөрү жатат.</p>
<p>Нарын дарыясы облус аркылуу агып өтөт. Анын үстүнө Токтогул суу сактагычы жана бир нече гидроэлектростанция курулган.</p>''',
            '''<p>На севере области — Чаткальский хребет и Таласский Ала-Тоо, на востоке — Ферганский хребет. А на юге лежат тёплые равнины Ферганской долины.</p>
<p>Через область течёт река Нарын. На ней построены Токтогульское водохранилище и несколько гидроэлектростанций.</p>''',
            '''<p>In the north are the Chatkal range and the Talas Ala-Too, and in the east the Fergana range. In the south lie the warm plains of the Fergana Valley.</p>
<p>The Naryn River flows through the region. The Toktogul Reservoir and several hydroelectric power stations have been built on it.</p>''',
        ),
        'nature': (
            '''<p>Арстанбапта дүйнөдөгү эң чоң жаңгак токойлорунун бири өсөт. Анда жаңгактан тышкары алма, алмурут жана башка жапайы мөмө-жемиштер да бар.</p>
<p>Сары-Челек — тоолордун арасындагы көгүш көл жана корук. Ал жерде сейрек кездешүүчү өсүмдүктөр жана жаныбарлар корголот.</p>''',
            '''<p>В Арсланбобе растёт один из крупнейших ореховых лесов в мире. Кроме грецкого ореха, там встречаются дикие яблони, груши и другие плодовые деревья.</p>
<p>Сары-Челек — голубое озеро среди гор и заповедник, где охраняют редкие растения и животных.</p>''',
            '''<p>Arslanbob has one of the largest walnut forests in the world. Besides walnuts, wild apples, pears and other fruit trees grow there.</p>
<p>Sary-Chelek is a blue lake among the mountains and a nature reserve that protects rare plants and animals.</p>''',
        ),
        'culture': (
            '''<p>Жалал-Абад шаары өзүнүн шыпаалуу минералдык булактары менен белгилүү, аларга дарылануу үчүн келишет.</p>
<p>Облуста кыргыздар менен катар өзбектер жана башка элдер жашайт. Түштүктүн базарлары, палоосу жана мөмө-жемиштери өзгөчө даамдуу.</p>''',
            '''<p>Город Джалал-Абад известен своими целебными минеральными источниками — сюда приезжают лечиться.</p>
<p>В области вместе с кыргызами живут узбеки и другие народы. Южные базары, плов и фрукты здесь особенно вкусные.</p>''',
            '''<p>The town of Jalal-Abad is known for its healing mineral springs, where people come for treatment.</p>
<p>Kyrgyz, Uzbeks and other peoples live in the region. Southern bazaars, plov and fruit here are especially tasty.</p>''',
        ),
        'area_km2': 33700,
        'facts': [
            (
                'Токтогул суу сактагычы — Борбордук Азиядагы эң чоң суу сактагычтардын бири.',
                'Токтогульское водохранилище — одно из крупнейших водохранилищ Центральной Азии.',
                'The Toktogul Reservoir is one of the largest reservoirs in Central Asia.',
            ),
            (
                'Арстанбаптын жаңгактары күзүндө терилет, ошондо токойго бүт үй-бүлөлөр чыгышат.',
                'Орехи в Арсланбобе собирают осенью — в это время в лес выходят целыми семьями.',
                'Walnuts in Arslanbob are gathered in autumn, when whole families go into the forest.',
            ),
        ],
    },
    'osh-region': {
        'summary': (
            'Ош облусу — түштүктөгү аймак. Ал Фергана өрөөнүнөн тартып бийик Алай тоолоруна чейин созулат.',
            'Ошская область — южный край, который тянется от Ферганской долины до высоких гор Алая.',
            'Osh Region is a southern region that stretches from the Fergana Valley up to the high Alai mountains.',
        ),
        'body': (
            '''<p>Ош облусу Кыргызстандын түштүгүндө жайгашкан. Анын түндүгүндө жылуу өрөөндөр жана бактар, ал эми түштүгүндө кар баскан бийик тоолор бар.</p>
<p>Облус Тажикстан, Өзбекстан жана Кытай менен чектешет. Ош шаары облустун ичинде жайгашкан, бирок өзүнчө шаар болуп эсептелет.</p>''',
            '''<p>Ошская область находится на юге Кыргызстана. На севере — тёплые долины и сады, а на юге — высокие заснеженные горы.</p>
<p>Область граничит с Таджикистаном, Узбекистаном и Китаем. Город Ош находится внутри области, но считается отдельным городом.</p>''',
            '''<p>Osh Region is in the south of Kyrgyzstan. In the north there are warm valleys and orchards, and in the south high snowy mountains.</p>
<p>The region borders Tajikistan, Uzbekistan and China. The city of Osh lies inside the region but is counted as a separate city.</p>''',
        ),
        'geography': (
            '''<p>Облустун түштүгүндө Алай өрөөнү жатат. Ал Алай жана Чоң Алай кырка тоолорунун ортосундагы кенен, бийик өрөөн.</p>
<p>Чоң Алайда, Тажикстан менен чек арада Ленин чокусу турат. Ал Памирдин эң бийик чокуларынын бири. Облус аркылуу Кара-Дарыя дарыясы агат.</p>''',
            '''<p>На юге области лежит Алайская долина — широкая высокогорная долина между Алайским и Заалайским хребтами.</p>
<p>На Заалайском хребте, на границе с Таджикистаном, стоит пик Ленина — одна из высочайших вершин Памира. Через область течёт река Карадарья.</p>''',
            '''<p>In the south of the region lies the Alai Valley, a wide high valley between the Alai and Trans-Alai ranges.</p>
<p>On the Trans-Alai range, on the border with Tajikistan, stands Lenin Peak, one of the highest peaks of the Pamirs. The Kara-Darya River flows through the region.</p>''',
        ),
        'nature': (
            '''<p>Алай өрөөнү — жайкысын жашыл жайлоолор менен капталган кооз жер. Ал жерден Ленин чокусунун ак кар баскан бети алыстан көрүнүп турат.</p>
<p>Облустун төмөн жактарында пахта, мөмө-жемиш жана жашылча өстүрүлөт. Тоолордо арча жана жаңгак токойлору кездешет.</p>''',
            '''<p>Алайская долина летом покрыта зелёными пастбищами. Отсюда далеко видна белоснежная стена пика Ленина.</p>
<p>В низинах области выращивают хлопок, фрукты и овощи. В горах встречаются можжевеловые и ореховые леса.</p>''',
            '''<p>In summer the Alai Valley is covered with green pastures, and the snowy wall of Lenin Peak can be seen from far away.</p>
<p>In the lowlands people grow cotton, fruit and vegetables. In the mountains there are juniper and walnut forests.</p>''',
        ),
        'culture': (
            '''<p>Өзгөн шаарында орто кылымда курулган кыштан жасалган мунара жана күмбөздөр сакталган. Алар Караханиддер мамлекетинин доорунан калган.</p>
<p>Облус аркылуу Памирге бара турган байыркы жол өтөт. Бул жерде жылкы, кой-эчки жана топоз багышат, ал эми жайлоолордо боз үйлөр тигилет.</p>''',
            '''<p>В городе Узген сохранились средневековый кирпичный минарет и мавзолеи времён государства Караханидов.</p>
<p>Через область проходит старинная дорога на Памир. Здесь разводят лошадей, овец, коз и яков, а на пастбищах ставят юрты.</p>''',
            '''<p>In the town of Uzgen you can see a medieval brick minaret and mausoleums from the time of the Karakhanid state.</p>
<p>An old road to the Pamirs crosses the region. People raise horses, sheep, goats and yaks, and set up yurts on the summer pastures.</p>''',
        ),
        'area_km2': 29200,
        'facts': [
            (
                'Ленин чокусунун бийиктиги 7000 метрден ашат. Аны тоо чыгуучулар дүйнө жүзүнөн келип багындырышат.',
                'Высота пика Ленина — больше 7000 метров. Покорять его приезжают альпинисты со всего мира.',
                'Lenin Peak is more than 7,000 metres high. Climbers come from all over the world to reach its top.',
            ),
            (
                'Алай өрөөнү деңиз деңгээлинен болжол менен 3000 метр бийиктикте жатат.',
                'Алайская долина лежит примерно на высоте 3000 метров над уровнем моря.',
                'The Alai Valley lies at about 3,000 metres above sea level.',
            ),
        ],
    },
    'batken': {
        'summary': (
            'Баткен облусу — өлкөнүн эң түштүк-батышындагы аймак. Ал өрүгү жана сейрек кездешүүчү айгүл гүлү менен белгилүү.',
            'Баткенская область — самый юго-западный край страны, знаменитый абрикосами и редким цветком айгуль.',
            'Batken Region is the south-western corner of the country, famous for its apricots and the rare aigul flower.',
        ),
        'body': (
            '''<p>Баткен облусу Кыргызстандын эң түштүк-батышында жайгашкан. Ал 1999-жылы Ош облусунан бөлүнүп, өзүнчө облус болгон.</p>
<p>Бул жерде жай ысык жана кургак, ошондуктан өрүк, жүзүм жана башка мөмө-жемиштер жакшы бышат.</p>''',
            '''<p>Баткенская область находится на самом юго-западе Кыргызстана. Она стала отдельной областью в 1999 году, выделившись из Ошской.</p>
<p>Лето здесь жаркое и сухое, поэтому отлично созревают абрикосы, виноград и другие фрукты.</p>''',
            '''<p>Batken Region is in the far south-west of Kyrgyzstan. It became a separate region in 1999, when it was split off from Osh Region.</p>
<p>Summers here are hot and dry, so apricots, grapes and other fruit ripen very well.</p>''',
        ),
        'geography': (
            '''<p>Облус Фергана өрөөнүнүн түштүк четинде жатат. Анын түштүгүндө Түркстан жана Алай кырка тоолору созулат.</p>
<p>Баткен Өзбекстан жана Тажикстан менен чектешет. Түркстан кырка тоосунда тик аскалуу бийик чокулар бар, аларга тоо чыгуучулар келишет.</p>''',
            '''<p>Область лежит на южном краю Ферганской долины. На юге её тянутся Туркестанский и Алайский хребты.</p>
<p>Баткен граничит с Узбекистаном и Таджикистаном. На Туркестанском хребте есть высокие отвесные скалы, куда приезжают альпинисты.</p>''',
            '''<p>The region lies on the southern edge of the Fergana Valley, with the Turkestan and Alai ranges to the south.</p>
<p>Batken borders Uzbekistan and Tajikistan. The Turkestan range has tall, steep rock walls that attract climbers.</p>''',
        ),
        'nature': (
            '''<p>Баткендин жанында, тоо этектеринде айгүл гүлү өсөт. Бул кызгылт-кызыл түстөгү сейрек гүл, ал жазында ачылат жана корголот.</p>
<p>Облустун өрөөндөрүндө өрүк бактары көп. Жазында алар ак-кызгылт гүлгө бөлөнүп, абдан кооз көрүнөт.</p>''',
            '''<p>Около Баткена в предгорьях растёт айгуль — редкий красно-оранжевый цветок, который распускается весной и находится под охраной.</p>
<p>В долинах области очень много абрикосовых садов. Весной они покрываются бело-розовыми цветами — это очень красиво!</p>''',
            '''<p>In the foothills near Batken grows the aigul, a rare red-orange flower that blooms in spring and is protected.</p>
<p>The valleys are full of apricot orchards. In spring they are covered in white and pink blossom — a beautiful sight!</p>''',
        ),
        'culture': (
            '''<p>Айгүл гүлү жөнүндө кыргыз элинде кооз уламыш бар. Жазында Баткенде ушул гүлгө арналган майрам өткөрүлөт.</p>
<p>Баткендин өрүгү бүт өлкөгө белгилүү. Жайында аны кургатып, кышка камдап коюшат жана башка өлкөлөргө сатышат.</p>''',
            '''<p>Об айгуле у кыргызов есть красивая легенда. В Баткене весной проводят праздник, посвящённый этому цветку.</p>
<p>Баткенские абрикосы знают по всей стране. Летом их сушат, запасают на зиму и продают в другие страны.</p>''',
            '''<p>The Kyrgyz have a beautiful legend about the aigul flower, and in spring Batken holds a festival in its honour.</p>
<p>Batken apricots are known all over the country. In summer they are dried, stored for winter and sold to other countries.</p>''',
        ),
        'area_km2': 17000,
        'facts': [
            (
                'Айгүл гүлү Баткен облусунун белгиси болуп калган.',
                'Цветок айгуль стал символом Баткенской области.',
                'The aigul flower has become a symbol of Batken Region.',
            ),
            (
                'Баткен — Кыргызстандын эң жаш облусу: ал 1999-жылы түзүлгөн.',
                'Баткенская — самая молодая область Кыргызстана: её создали в 1999 году.',
                'Batken is the youngest region of Kyrgyzstan: it was created in 1999.',
            ),
        ],
    },
    'bishkek': {
        'summary': (
            'Бишкек — Кыргызстандын борбору жана эң чоң шаары. Ал Чүй өрөөнүндө, тоолордун этегинде жайгашкан.',
            'Бишкек — столица и самый большой город Кыргызстана. Он стоит в Чуйской долине у подножия гор.',
            'Bishkek is the capital and largest city of Kyrgyzstan. It lies in the Chuy Valley at the foot of the mountains.',
        ),
        'body': (
            '''<p>Бишкек — өлкөнүн борбору. Бул жерде Жогорку Кеңеш, министрликтер, университеттер, театрлар жана музейлер жайгашкан.</p>
<p>Шаар көчөлөрүндө дарак көп, ошондуктан аны жашыл шаар деп аташат. Ачык күнү шаардын каалаган жеринен түштүктөгү кар баскан тоолор көрүнөт.</p>''',
            '''<p>Бишкек — столица страны. Здесь работают парламент (Жогорку Кенеш), министерства, университеты, театры и музеи.</p>
<p>На улицах города много деревьев, поэтому его называют зелёным городом. В ясный день почти отовсюду видны снежные горы на юге.</p>''',
            '''<p>Bishkek is the capital of the country. It is home to the parliament (the Jogorku Kenesh), ministries, universities, theatres and museums.</p>
<p>The streets are full of trees, so it is often called a green city. On a clear day you can see the snowy mountains to the south from almost anywhere.</p>''',
        ),
        'geography': (
            '''<p>Бишкек Чүй өрөөнүндө, Кыргыз Ала-Тоосунун этегинде, деңиз деңгээлинен болжол менен 800 метр бийиктикте жайгашкан.</p>
<p>Шаар аркылуу Ала-Арча жана Аламүдүн суулары агат. Шаардан Ала-Арча улуттук паркына чейин бир сааттай эле жол.</p>''',
            '''<p>Бишкек расположен в Чуйской долине у подножия Кыргызского Ала-Тоо, примерно на высоте 800 метров над уровнем моря.</p>
<p>Через город текут реки Ала-Арча и Аламедин. От города до национального парка Ала-Арча — около часа езды.</p>''',
            '''<p>Bishkek lies in the Chuy Valley at the foot of the Kyrgyz Ala-Too range, at about 800 metres above sea level.</p>
<p>The Ala-Archa and Alamedin rivers run through the city. Ala-Archa National Park is only about an hour’s drive away.</p>''',
        ),
        'nature': (
            '''<p>Бишкекте көп парктар жана бактар бар, мисалы, Дубовый парк жана Панфилов паркы. Ботаникалык бак да бар.</p>
<p>Шаардан чыкпай туруп эле Ала-Тоо кырка тоосун көрүүгө болот. Дем алыш күндөрү шаар тургундары таза аба жутуу үчүн Ала-Арча жана Аламүдүн капчыгайларына барышат.</p>''',
            '''<p>В Бишкеке много парков и скверов, например Дубовый парк и парк Панфилова. Есть и ботанический сад.</p>
<p>Горы Ала-Тоо видны прямо из города. В выходные горожане ездят в ущелья Ала-Арча и Аламедин подышать горным воздухом.</p>''',
            '''<p>Bishkek has many parks and squares, such as Oak Park and Panfilov Park, as well as a botanical garden.</p>
<p>The Ala-Too mountains are visible right from the city. At weekends people go to the Ala-Archa and Alamedin gorges for fresh mountain air.</p>''',
        ),
        'culture': (
            '''<p>Шаардын борборунда Ала-Тоо аянты жайгашкан. Анын жанында Тарых музейи турат. Бул жерде майрамдар жана салтанаттар өткөрүлөт.</p>
<p>Бишкек мурун Пишпек деп аталган, андан кийин көп жылдар бою Фрунзе деп аталып келген. 1991-жылы шаарга Бишкек деген ат берилген. Ош базары жана Дордой базары — шаардын белгилүү базарлары.</p>''',
            '''<p>В центре города находится площадь Ала-Тоо, рядом — Исторический музей. Здесь проходят праздники и торжества.</p>
<p>Раньше город назывался Пишпек, потом много лет — Фрунзе, а в 1991 году получил имя Бишкек. Ошский базар и рынок «Дордой» — самые известные базары города.</p>''',
            '''<p>In the city centre is Ala-Too Square, with the History Museum next to it. Celebrations and ceremonies take place here.</p>
<p>The city was once called Pishpek, then for many years Frunze, and in 1991 it was renamed Bishkek. Osh Bazaar and Dordoi Bazaar are its best-known markets.</p>''',
        ),
        'area_km2': None,
        'facts': [
            (
                'Бишкек 1926-жылдан 1991-жылга чейин Фрунзе деп аталган.',
                'С 1926 по 1991 год Бишкек назывался Фрунзе.',
                'From 1926 to 1991 Bishkek was called Frunze.',
            ),
            (
                'Бишкек Казакстан менен чек арага абдан жакын жайгашкан.',
                'Бишкек расположен совсем недалеко от границы с Казахстаном.',
                'Bishkek lies very close to the border with Kazakhstan.',
            ),
        ],
    },
    'osh-city': {
        'summary': (
            'Ош — Борбордук Азиядагы эң байыркы шаарлардын бири жана Кыргызстандын экинчи чоң шаары.',
            'Ош — один из древнейших городов Центральной Азии и второй по величине город Кыргызстана.',
            'Osh is one of the oldest cities in Central Asia and the second-largest city in Kyrgyzstan.',
        ),
        'body': (
            '''<p>Ош Кыргызстандын түштүгүндө, Фергана өрөөнүнүн чет жакасында жайгашкан. Аны көп учурда «түштүк борбору» деп аташат.</p>
<p>Шаардын ортосунда ыйык Сулайман-Тоо турат. 2000-жылы Ош шаарынын 3000 жылдыгы белгиленген.</p>''',
            '''<p>Ош находится на юге Кыргызстана, на краю Ферганской долины. Его часто называют «южной столицей».</p>
<p>Посреди города возвышается священная гора Сулайман-Тоо. В 2000 году Ош отметил своё 3000-летие — представь, какой это древний город!</p>''',
            '''<p>Osh lies in the south of Kyrgyzstan, on the edge of the Fergana Valley. It is often called the “southern capital”.</p>
<p>In the middle of the city rises the sacred mountain Sulaiman-Too. In 2000 Osh celebrated its 3,000th anniversary.</p>''',
        ),
        'geography': (
            '''<p>Шаар аркылуу Ак-Буура дарыясы агат. Ош Өзбекстан менен чек арага жакын жайгашкан.</p>
<p>Байыркы убакта Ош Улуу Жибек жолундагы маанилүү шаар болгон: бул жерде соодагерлер Фергана өрөөнүнөн тоолор аркылуу Кашкарга бара турган жолго чыгышкан.</p>''',
            '''<p>Через город течёт река Ак-Буура. Ош расположен недалеко от границы с Узбекистаном.</p>
<p>В древности Ош был важным городом на Великом Шёлковом пути: отсюда купцы из Ферганской долины отправлялись через горы в сторону Кашгара.</p>''',
            '''<p>The Ak-Buura River flows through the city. Osh lies close to the border with Uzbekistan.</p>
<p>In ancient times Osh was an important stop on the Great Silk Road: merchants set off from here across the mountains towards Kashgar.</p>''',
        ),
        'nature': (
            '''<p>Ошто жай узак жана жылуу болот. Шаардын айланасында бактар көп, базарларда мөмө-жемиш абдан арзан жана ширелүү.</p>
<p>Шаардан анча алыс эмес жерде Алай тоолору башталат. Сулайман-Тоонун чокусунан бүт шаар жана алыскы тоолор көрүнөт.</p>''',
            '''<p>Лето в Оше долгое и тёплое. Вокруг города много садов, а на базарах полно сочных фруктов.</p>
<p>Недалеко от города начинаются Алайские горы. С вершины Сулайман-Тоо виден весь город и далёкие горы.</p>''',
            '''<p>Summers in Osh are long and warm. There are many orchards around the city, and the bazaars are full of juicy fruit.</p>
<p>The Alai mountains begin not far away. From the top of Sulaiman-Too you can see the whole city and the distant peaks.</p>''',
        ),
        'culture': (
            '''<p>Оштогу Жайма базары — Борбордук Азиядагы эң чоң жана эң эски базарлардын бири. Анда жашылча, мөмө-жемиш, дан, кийим жана кол өнөрчүлүк буюмдары сатылат.</p>
<p>Ошто кыргыздар, өзбектер жана башка элдер жашайт. Шаардын тамак-ашы, мисалы, Ош палоосу бүт өлкөгө белгилүү.</p>''',
            '''<p>Ошский базар Жайма — один из самых больших и старинных базаров Центральной Азии. Здесь продают овощи, фрукты, зерно, одежду и изделия мастеров.</p>
<p>В Оше живут кыргызы, узбеки и другие народы. Ошский плов знают по всей стране.</p>''',
            '''<p>Osh’s Jayma Bazaar is one of the biggest and oldest markets in Central Asia. It sells vegetables, fruit, grain, clothes and handicrafts.</p>
<p>Kyrgyz, Uzbeks and other peoples live in Osh, and Osh plov is famous all over the country.</p>''',
        ),
        'area_km2': None,
        'facts': [
            (
                'Сулайман-Тоо 2009-жылы ЮНЕСКОнун Бүткүл дүйнөлүк мурастар тизмесине кирген.',
                'В 2009 году Сулайман-Тоо включили в список Всемирного наследия ЮНЕСКО.',
                'In 2009 Sulaiman-Too was added to the UNESCO World Heritage List.',
            ),
            (
                'Ош — Кыргызстандагы калкынын саны боюнча экинчи шаар.',
                'Ош — второй по числу жителей город Кыргызстана.',
                'Osh is the second-largest city in Kyrgyzstan by population.',
            ),
        ],
    },
}

PLACES = {
    'issyk-kul-lake': {
        'summary': (
            'Ысык-Көл — Кыргызстандын эң чоң көлү жана дүйнөдөгү эң чоң тоо көлдөрүнүн бири.',
            'Иссык-Куль — самое большое озеро Кыргызстана и одно из крупнейших горных озёр мира.',
            'Issyk-Kul is the largest lake in Kyrgyzstan and one of the largest mountain lakes in the world.',
        ),
        'body': (
            '''<p>Ысык-Көл Теңир-Тоонун тоолорунун арасында, деңиз деңгээлинен болжол менен 1600 метр бийиктикте жатат. Анын түндүгүндө Күнгөй Ала-Тоо, түштүгүндө Тескей Ала-Тоо кырка тоолору турат.</p>
<p>Көл абдан терең: анын эң терең жери 600 метрден ашат. Көлгө көптөгөн дарыялар куят, бирок андан бир да дарыя агып чыкпайт. Ошондуктан анын суусу бир аз туздуу.</p>
<p>Ысык-Көл кышында тоңбойт, ошондуктан ага «ысык көл» деген ат берилген. Жайында анын жээктерине эс алуучулар көп келишет, кумдуу пляждарда балдар ойношот.</p>
<p>Көлдүн жээгинде байыркы петроглифтер, кербен жолдорунун издери жана кыргыз элинин уламыштары көп. Сен Ысык-Көлдө сүзүп көрдүң беле?</p>''',
            '''<p>Иссык-Куль лежит среди гор Тянь-Шаня, примерно на высоте 1600 метров над уровнем моря. С севера его окружает хребет Кюнгёй Ала-Тоо, а с юга — Терскей Ала-Тоо.</p>
<p>Озеро очень глубокое: в самом глубоком месте больше 600 метров. В него впадает множество рек, но ни одна не вытекает. Поэтому вода в Иссык-Куле немного солёная.</p>
<p>Иссык-Куль не замерзает даже зимой — отсюда и название «горячее озеро». Летом на его берега приезжает множество отдыхающих, а дети играют на песчаных пляжах.</p>
<p>На берегах озера много древних петроглифов, следов караванных путей и кыргызских легенд. А ты уже купался в Иссык-Куле?</p>''',
            '''<p>Issyk-Kul lies among the Tian Shan mountains at about 1,600 metres above sea level, between the Kungey Ala-Too range to the north and the Terskey Ala-Too range to the south.</p>
<p>The lake is very deep — more than 600 metres at its deepest point. Many rivers flow into it, but none flow out. That is why its water is slightly salty.</p>
<p>Issyk-Kul does not freeze even in winter, which is how it got its name, “warm lake”. In summer many holidaymakers come to its shores, and children play on the sandy beaches.</p>
<p>Along the shores there are ancient petroglyphs, traces of caravan routes and many Kyrgyz legends. Have you ever swum in Issyk-Kul?</p>''',
        ),
        'facts': [
            (
                'Ысык-Көлгө көп дарыя куят, бирок андан бир да дарыя агып чыкпайт.',
                'В Иссык-Куль впадает много рек, но ни одна из него не вытекает.',
                'Many rivers flow into Issyk-Kul, but none flow out of it.',
            ),
            (
                'Ысык-Көл кышында да тоңбойт.',
                'Иссык-Куль не замерзает даже зимой.',
                'Issyk-Kul does not freeze even in winter.',
            ),
            (
                'Чолпон-Атада ташка тартылган байыркы сүрөттөр — петроглифтер сакталган.',
                'В Чолпон-Ате сохранились древние рисунки на камнях — петроглифы.',
                'Ancient pictures carved on stones — petroglyphs — survive in Cholpon-Ata.',
            ),
        ],
    },
    'son-kul-lake': {
        'summary': (
            'Соң-Көл — Нарын облусундагы, болжол менен 3000 метр бийиктикте жаткан тоо көлү. Анын айланасы жайлоолор менен курчалган.',
            'Сон-Куль — высокогорное озеро в Нарынской области на высоте около 3000 метров, окружённое летними пастбищами.',
            'Son-Kul is a high mountain lake in Naryn Region, at about 3,000 metres, surrounded by summer pastures.',
        ),
        'body': (
            '''<p>Соң-Көл — Нарын облусундагы бийик тоолуу көл. Ал деңиз деңгээлинен болжол менен 3000 метр бийиктикте жатат жана ар тараптан тоолор менен курчалган.</p>
<p>Көлдүн айланасында кенен жайлоолор бар. Жайында бул жерге малчылар малын айдап келишет, жээкте ак боз үйлөр тигилет. Ал жерде кымыз ичип, ат минип, жылдыздарга толгон асманды көрүүгө болот.</p>
<p>Соң-Көлдө кыш абдан суук жана узун. Көл кышында тоңуп калат, ал эми жай кыска жана салкын.</p>
<p>Бул жер көчмөн жашоонун салттарын өз көзүң менен көрө турган сейрек жерлердин бири. Сен боз үйдө түнөп көргүң келеби?</p>''',
            '''<p>Сон-Куль — высокогорное озеро в Нарынской области. Оно лежит примерно на высоте 3000 метров над уровнем моря и со всех сторон окружено горами.</p>
<p>Вокруг озера раскинулись широкие пастбища — жайлоо. Летом сюда пригоняют скот, а на берегу ставят белые юрты. Здесь можно попробовать кумыс, покататься на лошади и увидеть небо, полное звёзд.</p>
<p>Зима на Сон-Куле очень холодная и долгая. Озеро зимой замерзает, а лето здесь короткое и прохладное.</p>
<p>Это одно из мест, где можно своими глазами увидеть традиции кочевой жизни. Хотел бы ты переночевать в юрте?</p>''',
            '''<p>Son-Kul is a high mountain lake in Naryn Region. It lies at about 3,000 metres above sea level and is surrounded by mountains on all sides.</p>
<p>Wide pastures called jailoo spread around the lake. In summer herders bring their animals here and white yurts appear along the shore. You can taste kymyz, ride a horse and see a sky full of stars.</p>
<p>Winter at Son-Kul is very cold and long. The lake freezes over, and the summer is short and cool.</p>
<p>It is one of the places where you can see nomadic traditions with your own eyes. Would you like to spend a night in a yurt?</p>''',
        ),
        'facts': [
            (
                'Соң-Көл — Ысык-Көлдөн кийинки Кыргызстандагы эң чоң көлдөрдүн бири.',
                'Сон-Куль — одно из крупнейших озёр Кыргызстана после Иссык-Куля.',
                'Son-Kul is one of the largest lakes in Kyrgyzstan after Issyk-Kul.',
            ),
            (
                'Соң-Көл кышында тоңуп калат, ал эми жайында анын жээгинде боз үйлөр тигилет.',
                'Зимой Сон-Куль замерзает, а летом на его берегах ставят юрты.',
                'Son-Kul freezes in winter, and in summer yurts are set up along its shores.',
            ),
        ],
    },
    'sulaiman-too': {
        'summary': (
            'Сулайман-Тоо — Ош шаарынын ортосундагы ыйык тоо жана Кыргызстандагы ЮНЕСКОнун Бүткүл дүйнөлүк мурасы.',
            'Сулайман-Тоо — священная гора в центре Оша, объект Всемирного наследия ЮНЕСКО.',
            'Sulaiman-Too is a sacred mountain in the middle of Osh and a UNESCO World Heritage Site.',
        ),
        'body': (
            '''<p>Сулайман-Тоо — Ош шаарынын так ортосунда көтөрүлүп турган аскалуу тоо. Анын бир нече чокусу бар, алардын үстүнөн бүт шаар көрүнөт.</p>
<p>Бул тоо миңдеген жылдар бою адамдар үчүн ыйык жер болуп келген. Анын аскаларында байыркы адамдар тарткан сүрөттөр — петроглифтер сакталган, тоонун боорунда ыйык үңкүрлөр жана сыйынуучу жайлар бар.</p>
<p>Тоонун боорундагы үңкүрдүн ичинде музей жайгашкан. Анда бул жердин тарыхы жана табияты жөнүндө айтылат.</p>
<p>2009-жылы Сулайман-Тоо ЮНЕСКОнун Бүткүл дүйнөлүк мурастар тизмесине кирген. Бул Кыргызстандын ушундай даражага ээ болгон биринчи эстелиги.</p>''',
            '''<p>Сулайман-Тоо — скалистая гора, которая поднимается прямо в центре Оша. У неё несколько вершин, и с них виден весь город.</p>
<p>Тысячи лет эта гора считается священной. На её скалах сохранились рисунки древних людей — петроглифы, а на склонах есть почитаемые пещеры и места паломничества.</p>
<p>Внутри пещеры на склоне горы устроен музей. В нём рассказывают об истории и природе этих мест.</p>
<p>В 2009 году Сулайман-Тоо включили в список Всемирного наследия ЮНЕСКО. Это первый объект Кыргызстана, получивший такое звание. Как думаешь, почему люди так долго считали эту гору особенной?</p>''',
            '''<p>Sulaiman-Too is a rocky mountain that rises right in the centre of Osh. It has several peaks, and from them you can see the whole city.</p>
<p>For thousands of years this mountain has been a sacred place. Ancient petroglyphs survive on its rocks, and on its slopes there are revered caves and places of pilgrimage.</p>
<p>A museum has been set up inside a cave on the mountainside. It tells about the history and nature of the area.</p>
<p>In 2009 Sulaiman-Too was added to the UNESCO World Heritage List — the first site in Kyrgyzstan to receive this status. Why do you think people have thought of this mountain as special for so long?</p>''',
        ),
        'facts': [
            (
                'Сулайман-Тоо — Кыргызстандан ЮНЕСКОнун Бүткүл дүйнөлүк мурастар тизмесине кирген биринчи эстелик.',
                'Сулайман-Тоо — первый объект Кыргызстана в списке Всемирного наследия ЮНЕСКО.',
                'Sulaiman-Too was the first site in Kyrgyzstan on the UNESCO World Heritage List.',
            ),
            (
                'Тоонун аскаларында байыркы петроглифтер сакталган.',
                'На скалах горы сохранились древние петроглифы.',
                'Ancient petroglyphs survive on the rocks of the mountain.',
            ),
            (
                'Тоонун боорундагы үңкүрдүн ичинде музей бар.',
                'Внутри пещеры на склоне горы находится музей.',
                'There is a museum inside a cave on the mountainside.',
            ),
        ],
    },
    'tash-rabat': {
        'summary': (
            'Таш-Рабат — Нарын облусундагы бийик тоолордо курулган байыркы таш кербен сарай.',
            'Таш-Рабат — старинный каменный караван-сарай высоко в горах Нарынской области.',
            'Tash-Rabat is an old stone caravanserai high in the mountains of Naryn Region.',
        ),
        'body': (
            '''<p>Таш-Рабат — Нарын облусунун Ат-Башы районундагы тоо капчыгайында жайгашкан таш имарат. Анын аты «таш үй» же «таш сарай» дегенди билдирет.</p>
<p>Ал Улуу Жибек жолунун бир тармагында турган кербен сарай болгон. Окумуштуулардын пикири боюнча, имараттын азыркы көрүнүшү болжол менен XV кылымга таандык. Бул жерде соодагерлер жана саякатчылар суук жана шамалдан жашынып эс алышкан.</p>
<p>Имарат жалпак таштардан курулган, анын ортосунда күмбөздүү чоң зал жана айланасында көптөгөн кичинекей бөлмөлөр бар. Ичине кирсең, байыркы кербенчилердин турмушун элестетүүгө болот.</p>
<p>Таш-Рабат — Кыргызстандагы эң жакшы сакталган байыркы имараттардын бири. Тоолордун арасында ушундай имаратты куруу оңой болгон эмес деп ойлойсуңбу?</p>''',
            '''<p>Таш-Рабат — каменное здание в горном ущелье Ат-Башинского района Нарынской области. Его название означает «каменное строение» или «каменный двор».</p>
<p>Это был караван-сарай на одном из ответвлений Великого Шёлкового пути. По мнению учёных, в нынешнем виде здание относится примерно к XV веку. Здесь купцы и путешественники прятались от холода и ветра и отдыхали в дороге.</p>
<p>Здание сложено из плоских камней: в центре — большой зал с куполом, а вокруг — много маленьких комнат. Зайдя внутрь, легко представить жизнь древних караванщиков.</p>
<p>Таш-Рабат — одно из лучше всего сохранившихся старинных зданий Кыргызстана. Как ты думаешь, легко ли было строить такой дом высоко в горах?</p>''',
            '''<p>Tash-Rabat is a stone building in a mountain gorge in At-Bashy district of Naryn Region. Its name means “stone building” or “stone inn”.</p>
<p>It was a caravanserai on one of the branches of the Great Silk Road. Scholars believe the building in its present form dates from around the 15th century. Merchants and travellers sheltered here from the cold and wind and rested on their journey.</p>
<p>It is built of flat stones, with a large domed hall in the centre and many small rooms around it. Step inside and you can easily imagine the life of the old caravan travellers.</p>
<p>Tash-Rabat is one of the best-preserved old buildings in Kyrgyzstan. Do you think it was easy to build something like this high in the mountains?</p>''',
        ),
        'facts': [
            (
                'Таш-Рабат деңиз деңгээлинен 3000 метрден ашык бийиктикте жайгашкан.',
                'Таш-Рабат стоит на высоте более 3000 метров над уровнем моря.',
                'Tash-Rabat stands more than 3,000 metres above sea level.',
            ),
            (
                'Кербен сарай — соодагерлер жана алардын төөлөрү, аттары түнөгөн жай.',
                'Караван-сарай — это место, где ночевали купцы со своими верблюдами и лошадьми.',
                'A caravanserai was a place where merchants stayed overnight with their camels and horses.',
            ),
        ],
    },
    'burana-tower': {
        'summary': (
            'Бурана мунарасы — Токмоктун жанындагы орто кылымдагы мунара. Ал байыркы Баласагын шаарынан калган.',
            'Башня Бурана — средневековый минарет возле Токмока, оставшийся от древнего города Баласагун.',
            'Burana Tower is a medieval minaret near Tokmok, left from the ancient city of Balasagun.',
        ),
        'body': (
            '''<p>Бурана мунарасы Чүй өрөөнүндө, Токмок шаарынын жанында турат. Ал XI кылымда кыштан курулган мунара.</p>
<p>Илгери бул жерде Баласагын шаары болгон. Ал Караханиддер мамлекетинин маанилүү шаарларынын бири эле. Ушул шаарда «Кутадгу билиг» деген атактуу китептин автору Жусуп Баласагын төрөлгөн.</p>
<p>Мурун мунара азыркыдан алда канча бийик болгон, бирок жер титирөөдөн улам анын үстүңкү бөлүгү кулап калган. Азыр мунаранын ичиндеги тепкичтер менен өйдө чыгып, айланадагы тоолорду жана талааларды көрүүгө болот.</p>
<p>Мунаранын жанында таш балбалдардын — байыркы адамдардын таштан жасалган элестеринин — чоң коллекциясы жана кичинекей музей бар.</p>''',
            '''<p>Башня Бурана стоит в Чуйской долине, недалеко от города Токмок. Это кирпичный минарет, построенный в XI веке.</p>
<p>Когда-то здесь был город Баласагун — один из важных городов государства Караханидов. Именно здесь родился Юсуф Баласагуни, автор знаменитой книги «Кутадгу билиг» («Благодатное знание»).</p>
<p>Раньше минарет был намного выше, но его верхняя часть обрушилась из-за землетрясения. Сегодня по узкой лестнице внутри башни можно подняться наверх и посмотреть на горы и поля вокруг.</p>
<p>Рядом с башней собрана большая коллекция балбалов — древних каменных изваяний людей, — а также работает небольшой музей. Попробуй посчитать, сколько им лет!</p>''',
            '''<p>Burana Tower stands in the Chuy Valley near the town of Tokmok. It is a brick minaret built in the 11th century.</p>
<p>Long ago this was the city of Balasagun, one of the important cities of the Karakhanid state. It was the birthplace of Yusuf Balasaguni, author of the famous book Kutadgu Bilig (“Wisdom of Royal Glory”).</p>
<p>The minaret used to be much taller, but its upper part collapsed in an earthquake. Today you can climb a narrow staircase inside the tower and look out over the mountains and fields.</p>
<p>Next to the tower there is a large collection of balbals — ancient stone figures of people — and a small museum.</p>''',
        ),
        'facts': [
            (
                'Бурана мунарасынын үстүңкү бөлүгү жер титирөөдөн кулап калган.',
                'Верхняя часть башни Бурана обрушилась во время землетрясения.',
                'The upper part of Burana Tower collapsed in an earthquake.',
            ),
            (
                'Жусуп Баласагын «Кутадгу билиг» китебин XI кылымда жазган.',
                'Юсуф Баласагуни написал книгу «Кутадгу билиг» в XI веке.',
                'Yusuf Balasaguni wrote Kutadgu Bilig in the 11th century.',
            ),
            (
                'Балбалдар — байыркы түрк доорунда коюлган таш эстеликтер.',
                'Балбалы — каменные изваяния, которые ставили в древнетюркскую эпоху.',
                'Balbals are stone figures erected in the ancient Turkic period.',
            ),
        ],
    },
    'arslanbob': {
        'summary': (
            'Арстанбап — Жалал-Абад облусундагы айыл жана дүйнөдөгү эң чоң жаңгак токойлорунун бири.',
            'Арсланбоб — село в Джалал-Абадской области и один из крупнейших ореховых лесов в мире.',
            'Arslanbob is a village in Jalal-Abad Region and home to one of the largest walnut forests in the world.',
        ),
        'body': (
            '''<p>Арстанбап — Бабаш-Ата тоолорунун этегинде жайгашкан чоң айыл. Анын айланасында кенен жаңгак-мөмө токою жайылып жатат.</p>
<p>Бул токой табигый жол менен өсүп чыккан, аны адамдар отургузган эмес. Анда жаңгактан тышкары жапайы алма, алмурут, алча жана башка мөмө-жемиш дарактары өсөт.</p>
<p>Күзүндө жаңгак бышканда айылдын тургундары токойго чыгып, түшүмдү чогултушат. Арстанбаптын жаңгагы бүт өлкөгө белгилүү.</p>
<p>Айылдын жанында кооз шаркыратмалар бар, аларды көрүүгө саякатчылар келишет. Мындай токойлор сейрек кездешет, ошондуктан аларды сактоо абдан маанилүү.</p>''',
            '''<p>Арсланбоб — большое село у подножия хребта Бабаш-Ата. Вокруг него раскинулся огромный орехово-плодовый лес.</p>
<p>Этот лес вырос сам, его не сажали люди. Кроме грецкого ореха, в нём растут дикие яблони, груши, алыча и другие плодовые деревья.</p>
<p>Осенью, когда орехи созревают, жители села выходят в лес собирать урожай. Орехи Арсланбоба знают по всей стране.</p>
<p>Рядом с селом есть красивые водопады, к ним приходят путешественники. Таких лесов в мире очень мало, поэтому их важно беречь. Как ты думаешь, что можно сделать, чтобы сохранить этот лес?</p>''',
            '''<p>Arslanbob is a large village at the foot of the Babash-Ata range. Around it spreads a huge walnut and fruit forest.</p>
<p>The forest grew naturally — people did not plant it. Besides walnuts, wild apples, pears, cherry plums and other fruit trees grow there.</p>
<p>In autumn, when the nuts are ripe, villagers go into the forest to gather the harvest. Arslanbob walnuts are known all over the country.</p>
<p>Near the village there are beautiful waterfalls that travellers come to see. Forests like this are rare in the world, so it is very important to protect them.</p>''',
        ),
        'facts': [
            (
                'Арстанбаптын жаңгак токою табигый жол менен өскөн.',
                'Ореховый лес Арсланбоба вырос естественным путём, его не сажали.',
                'The Arslanbob walnut forest grew naturally; it was not planted.',
            ),
            (
                'Токойдо жаңгактан тышкары жапайы алма жана алмурут дарактары да өсөт.',
                'В лесу растут не только орехи, но и дикие яблони и груши.',
                'Besides walnuts, wild apple and pear trees grow in the forest.',
            ),
        ],
    },
    'ala-archa': {
        'summary': (
            'Ала-Арча — Бишкекке жакын жайгашкан улуттук парк. Анда бийик тоолор, мөңгүлөр жана арча токойлору бар.',
            'Ала-Арча — национальный парк рядом с Бишкеком с высокими горами, ледниками и можжевеловыми лесами.',
            'Ala-Archa is a national park near Bishkek, with high mountains, glaciers and juniper forests.',
        ),
        'body': (
            '''<p>Ала-Арча улуттук паркы Бишкектин түштүгүндө, Кыргыз Ала-Тоосунун капчыгайында жайгашкан. Шаардан ага чейин бир сааттай эле жол.</p>
<p>Парктын аты ушул жерде көп өскөн арча деген дарактан келип чыккан. Капчыгай аркылуу Ала-Арча дарыясы шаркырап агат, анын суусу мөңгүлөрдөн башталат.</p>
<p>Паркта бийик чокулар жана мөңгүлөр бар. Бул жерге жөө басуучулар, тоо чыгуучулар жана жөн эле таза аба жуткусу келгендер келишет. Тоолордо тоо теке жана башка жапайы жаныбарлар жашайт.</p>
<p>Ала-Арча — тоолор менен таанышууну баштоо үчүн эң ыңгайлуу жер. Бирок тоодо дайыма чоңдор менен жүрүү жана жылуу кийим алуу керек!</p>''',
            '''<p>Национальный парк Ала-Арча находится к югу от Бишкека, в ущелье хребта Кыргызский Ала-Тоо. От города до него около часа езды.</p>
<p>Своё название парк получил от арчи — так по-кыргызски называют можжевельник, который здесь растёт. По ущелью бурлит река Ала-Арча, которая начинается у ледников.</p>
<p>В парке есть высокие вершины и ледники. Сюда приезжают туристы, альпинисты и просто те, кто хочет подышать свежим воздухом. В горах живут горные козлы и другие дикие животные.</p>
<p>Ала-Арча — отличное место, чтобы начать знакомство с горами. Только помни: в горы нужно ходить вместе со взрослыми и брать тёплую одежду!</p>''',
            '''<p>Ala-Archa National Park lies south of Bishkek in a gorge of the Kyrgyz Ala-Too range, about an hour’s drive from the city.</p>
<p>The park is named after the archa — the Kyrgyz word for juniper, which grows here. The Ala-Archa River rushes through the gorge, starting from the glaciers.</p>
<p>The park has high peaks and glaciers. Hikers, climbers and people who simply want fresh air come here. Ibex and other wild animals live in the mountains.</p>
<p>Ala-Archa is a great place to start getting to know the mountains. Just remember: always go with adults and take warm clothes!</p>''',
        ),
        'facts': [
            (
                'Арча — тоолордо өсүүчү ийне жалбырактуу дарак. Орусча аны «можжевельник» деп аташат.',
                '«Арча» по-кыргызски значит «можжевельник».',
                '“Archa” is the Kyrgyz word for juniper.',
            ),
            (
                'Парктагы Ак-Сай мөңгүсүнө тоо чыгуучулар көп барышат.',
                'К леднику Ак-Сай в парке часто поднимаются альпинисты.',
                'Climbers often go up to the Ak-Sai Glacier in the park.',
            ),
        ],
    },
    'sary-chelek': {
        'summary': (
            'Сары-Челек — Жалал-Абад облусундагы тоо көлү жана биосфералык корук.',
            'Сары-Челек — горное озеро и биосферный заповедник в Джалал-Абадской области.',
            'Sary-Chelek is a mountain lake and biosphere reserve in Jalal-Abad Region.',
        ),
        'body': (
            '''<p>Сары-Челек — Чаткал кырка тоосунун тоолорунун арасында жайгашкан кооз көл. Анын суусу көгүш-жашыл түстө, айланасында карагай, жаңгак жана мөмө дарактары өскөн токойлор бар.</p>
<p>Көл илгери тоодон кулаган чоң таштар суунун жолун тосуп калгандан кийин пайда болгон деп эсептелет. Ал терең жана тунук.</p>
<p>Көлдүн айланасы — биосфералык корук. Бул жерде сейрек кездешүүчү өсүмдүктөр жана жаныбарлар, мисалы, аюу жана көптөгөн куштар корголот. Корукта аң уулоого жана дарак кесүүгө болбойт.</p>
<p>Сары-Челектин жанында дагы бир нече кичинекей көлдөр бар. Ушундай жерлерди сактоо эмне үчүн маанилүү деп ойлойсуң?</p>''',
            '''<p>Сары-Челек — красивое озеро среди гор Чаткальского хребта. Вода в нём сине-зелёная, а вокруг растут леса из ели, ореха и плодовых деревьев.</p>
<p>Считается, что озеро появилось давным-давно, когда огромный обвал горных пород перегородил путь реке. Озеро глубокое и очень прозрачное.</p>
<p>Вокруг озера — биосферный заповедник. Здесь охраняют редкие растения и животных: например медведи и множество птиц. В заповеднике нельзя охотиться и рубить деревья.</p>
<p>Рядом с Сары-Челеком есть ещё несколько маленьких озёр. Как ты думаешь, почему так важно сохранять такие места?</p>''',
            '''<p>Sary-Chelek is a beautiful lake among the mountains of the Chatkal range. Its water is blue-green, and it is surrounded by forests of spruce, walnut and fruit trees.</p>
<p>The lake is thought to have formed long ago when a huge landslide blocked a river. It is deep and very clear.</p>
<p>The area around the lake is a biosphere reserve. Rare plants and animals are protected here, including bears and many birds. Hunting and cutting trees are not allowed in the reserve.</p>
<p>There are several smaller lakes near Sary-Chelek too. Why do you think it is so important to protect places like this?</p>''',
        ),
        'facts': [
            (
                'Сары-Челек коругу ЮНЕСКОнун биосфералык корууларынын тизмесине кирет.',
                'Заповедник Сары-Челек входит во всемирную сеть биосферных резерватов ЮНЕСКО.',
                'The Sary-Chelek Reserve is part of UNESCO’s World Network of Biosphere Reserves.',
            ),
            (
                'Сары-Челек көлү тоодон кулаган таштар дарыяны тосуп калгандан пайда болгон деп эсептелет.',
                'Считается, что озеро Сары-Челек образовалось, когда горный обвал перегородил реку.',
                'Lake Sary-Chelek is thought to have formed when a landslide dammed a river.',
            ),
        ],
    },
}
