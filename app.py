from Chat import Chat
import gradio as gr
import random
import time

pairs = (
    (
        r".*dasturlash.*nima.*",
        (
            "Dasturlash - bu kompyuterlarga ma'lum buyruqlarni beradigan jarayondir.",
            "Dasturlash orqali turli muammolarni hal qilishingiz mumkin.",
            "Dasturlash kompyuterning vazifalarni bajarish uchun dasturlangan ko'rsatmalarni ishlatadi.",
        ),
    ),
    (
        r".*python.*nimaga.*ishlatiladi.*",
        (
            "Python juda ko'p sohalarda, jumladan, veb-dasturlash, AI, avtomatlashtirishda qo'llaniladi.",
            "Python oddiyligi va keng imkoniyatlari tufayli ishlatiladi.",
            "Python - bu kuchli va ko'p qirrali dasturlash tili.",
        ),
    ),
    (
        r".*java.*va.*farqi.*",
        (
            "Java umumiy dasturlash uchun ishlatiladi, boshqa tillar veb-ishlab chiqishga mos.",
            "Java ko'p platformalarda ishlaydi va keng qo'llaniladi.",
        ),
    ),
    (
        r".*AI.*nima.*",
        (
            "AI, ya'ni sun'iy intellekt, kompyuter tizimlariga insoniy fikrlash va qaror qabul qilish qobiliyatini beradi.",
            "AI texnologiyasi avtomatlashtirilgan tizimlar va aqlli yordamchilarda qo'llaniladi.",
        ),
    ),
    (
        r".*tarmoq.*neural.*",
        (
            "Neural tarmoq inson miyasi kabi ishlaydigan tizim bo'lib, mashina o'rganish uchun muhim.",
            "Neural tarmoqlar katta ma'lumotlarni o'rganish va bashorat qilishda ishlatiladi.",
        ),
    ),

        (
        r".*python.*nimaga.*ishlatiladi.*",
        (
            "Python veb-ishlab chiqish, sun'iy intellekt, avtomatlashtirish, ilmiy hisoblash va boshqa ko'p sohalarda ishlatiladi.",
            "Python oddiy va kuchli dasturlash tili bo'lib, ko'p sohalarda keng qo'llaniladi.",
            "Python o'rganish oson va ko'p platformalarda qo'llanilishi mumkin.",
        ),
    ),
    
    # Java va boshqa tillar o'rtasidagi farq nima?
    (
        r".*java.*va.*(.*)farqi.*",
        (
            "Java umumiy dasturlash uchun ishlatiladi, %1 esa ko'proq veb-ishlab chiqishda qo'llaniladi.",
            "Java va %1 o'rtasidagi farq ularning qo'llanilish sohasida va sintaksisida bo'lishi mumkin.",
            "Java %1 bilan taqqoslaganda ko'proq platformalarda ishlaydi.",
        ),
    ),
    
    # C++ nima uchun ishlatiladi?
    (
        r".*c\+\+.*nimaga.*ishlatiladi.*",
        (
            "C++ odatda yuqori tezlik talab qilinadigan tizimlar va ilovalar, shuningdek, o'yinlar va kompyuter grafikasi uchun ishlatiladi.",
            "C++ tilining tezligi va samaradorligi uni katta miqdordagi ma'lumotlarni qayta ishlashda muhim qiladi.",
        ),
    ),
    
    # AI (sun'iy intellekt) nima?
    (
        r".*ai.*nima.*",
        (
            "AI, ya'ni sun'iy intellekt, bu kompyuter tizimlariga insoniy fikrlash va qaror qabul qilish qobiliyatlarini beradigan texnologiya.",
            "AI o'rganish algoritmlarini qo'llash orqali avtomatlashtirish va tahlillarni kuchaytirishga yordam beradi.",
            "AI texnologiyalari ko'plab sohalarda, jumladan, avtomatlashtirilgan tizimlar va robototexnika sohalarida qo'llaniladi.",
        ),
    ),
    
    # Neural tarmoq nima?
    (
        r".*neural.*tarmoq.*nima.*",
        (
            "Neural tarmoq bu biologik miya tarmoqlarini taqlid qiladigan mashina o'rganish modeli bo'lib, katta hajmdagi ma'lumotlarni o'rganishga yordam beradi.",
            "Neural tarmoqlar ko'p qatlamli o'rganish jarayonini ishlatib, murakkab muammolarni hal qilish uchun ishlatiladi.",
            "Neural tarmoqlar katta hajmdagi ma'lumotlar bilan ishlash va bashorat qilish imkonini beradi.",
        ),
    ),
    
    # O'yin dasturlash haqida
    (
        r".*o'yin.*dasturlash.*",
        (
            "O'yin dasturlash odatda C++ va Unity kabi platformalar yordamida amalga oshiriladi.",
            "O'yin dasturlashda 3D modellar, fizikasi va animatsiyalar bilan ishlash juda muhimdir.",
        ),
    ),
    
    # Backend va Frontend farqi nima?
    (
        r".*backend.*frontend.*farqi.*",
        (
            "Backend - bu server tomonidagi dasturlash, frontend esa foydalanuvchi interfeysi bilan bog'liq dasturlashdir.",
            "Backend tizimning logik qismlarini boshqaradi, frontend esa foydalanuvchiga ko'rinadigan qismdir.",
            "Frontend HTML, CSS, JavaScript kabi texnologiyalarni qo'llaydi, backend esa Python, Node.js va boshqalarni qo'llaydi.",
        ),
    ),
    
    # Mashina o'rganishi nima?
    (
        r".*mashina.*o'rganish.*nima.*",
        (
            "Mashina o'rganishi - bu kompyuter tizimlarining o'z tajribasidan o'rganib, qaror qabul qilishni o'rgatuvchi texnologiya.",
            "Mashina o'rganishi algoritmlari ma'lumotlardan tahlil qilib, bashoratlarni yaxshilashga yordam beradi.",
            "Mashina o'rganishi orqali tizimlar o'z ma'lumotlaridan avtomatik ravishda yangi bilimlarni o'zlashtirishi mumkin.",
        ),
    ),
    
    # OOP (Object-Oriented Programming) nima?
    (
        r".*oop.*nima.*",
        (
            "OOP (Object-Oriented Programming) - bu dasturlash usuli bo'lib, ob'ektlar va ularning o'zaro ta'siri asosida dasturlarni yaratishga imkon beradi.",
            "OOP tizimlarida har bir ob'ekt o'ziga xos xususiyatlarga va metodlarga ega bo'ladi.",
            "OOPning asosiy prinsiplari: inheritance (meros), polymorphism (ko'p shakllilik), encapsulation (inkapsulyatsiya) va abstraction (abstraktsiya).",
        ),
    ),
    
    # Framework nima?
    (
        r".*framework.*nima.*",
        (
            "Framework - bu dasturlashda ishni tezlashtirish va qulaylashtirish uchun tayyor kodlar to'plami.",
            "Framework yordamida siz asosiy funksiyalarni o'zingiz yozmasdan, ularni foydalanishga tayyor ko'rinishda olishingiz mumkin.",
            "Mashhur frameworklardan biri Django (Python uchun), React (JavaScript uchun).",
        ),
    ),

        (
        r".*algoritm.*nima.*",
        (
            "Algoritm - bu muayyan muammoni hal qilish uchun bajariladigan aniq va ketma-ket ko'rsatmalar to'plami.",
            "Algoritmlar dastur yoki tizimning qanday ishlashini boshqaradi va ko'plab sohalarda qo'llaniladi.",
            "Algoritmlar ma'lum vazifalarni bajarish uchun tuziladi va ularning samaradorligi muhim.",
        ),
    ),

    # Data structures nima?
    (
        r".*data.*structures.*nima.*",
        (
            "Data structures (ma'lumot tuzilmalari) - bu ma'lumotlarni saqlash va boshqarish usullari bo'lib, samarali dasturlash uchun zarurdir.",
            "Eng ko'p ishlatiladigan ma'lumot tuzilmalari orasida massivlar, ro'yxatlar, to'plamlar va daraxtlar bor.",
            "Data structures dasturlarning tezkor va samarali ishlashini ta'minlaydi.",
        ),
    ),

    # Kompyuter tarmoqlari nima?
    (
        r".*kompyuter.*tarmoqlari.*nima.*",
        (
            "Kompyuter tarmoqlari - bu bir nechta kompyuterlar yoki qurilmalar o'rtasida ma'lumotlarni almashish uchun o'rnatilgan tizimdir.",
            "Kompyuter tarmoqlari lokal yoki global bo'lishi mumkin va ular orqali ma'lumotlar uzatiladi.",
            "Internet eng katta va mashhur kompyuter tarmoqlaridan biridir.",
        ),
    ),

    # TCP/IP protokoli nima?
    (
        r".*tcp/ip.*protokol.*nima.*",
        (
            "TCP/IP - bu internet va tarmoqlarda ma'lumotlarni qanday uzatilishini boshqaradigan protokollar to'plami.",
            "TCP/IP protokoli paketlarni boshqarish va ulanishlar o'rnatish uchun ishlatiladi.",
            "Bu protokolning asosiy vazifasi tarmoqlarda ma'lumotlarni xavfsiz va aniq uzatishdir.",
        ),
    ),

    # Bulutli hisoblash nima?
    (
        r".*bulut.*hisoblash.*nima.*",
        (
            "Bulutli hisoblash - bu internet orqali saqlash, dasturlar yoki xizmatlardan foydalanish texnologiyasi.",
            "Bulutli hisoblash foydalanuvchilarga katta miqdordagi ma'lumotlarni uzoqdan boshqarishga imkon beradi.",
            "Google Drive yoki Dropbox kabi xizmatlar bulutli hisoblashning namunalaridir.",
        ),
    ),

    # Kriptografiya nima?
    (
        r".*kriptografiya.*nima.*",
        (
            "Kriptografiya - bu ma'lumotlarni shifrlash va himoya qilish texnologiyasi, odatda xavfsizlik uchun ishlatiladi.",
            "Kriptografiya yordamida ma'lumotlarni maxfiy saqlash va faqat ruxsat etilgan shaxslarga ochish mumkin.",
            "Kriptografiya elektron tijorat, banking va boshqa sohalarda xavfsizlikni ta'minlaydi.",
        ),
    ),

    # Big Data nima?
    (
        r".*big.*data.*nima.*",
        (
            "Big Data - bu katta hajmdagi ma'lumotlar to'plami bo'lib, ularni tahlil qilish va boshqarish an'anaviy usullar bilan murakkab bo'ladi.",
            "Big Data ko'pincha sun'iy intellekt va mashina o'rganish bilan birgalikda ishlatiladi.",
            "Big Data texnologiyalari ma'lumotlar tahlilini osonlashtiradi va katta hajmdagi ma'lumotlarni qayta ishlash imkonini beradi.",
        ),
    ),

    # DNS nima?
    (
        r".*dns.*nima.*",
        (
            "DNS (Domain Name System) - bu domen nomlarini IP-manzillarga o'zgartirishga xizmat qiladigan tizimdir.",
            "DNS orqali sayt nomlari IP-manzillarga mos keladi va kompyuterlarga tarmoqlar orqali ulanish imkonini beradi.",
            "Masalan, sizning brauzeringizda 'google.com' ni yozsangiz, DNS ushbu domenni IP-manzilga o'zgartiradi.",
        ),
    ),

    # Hashing nima?
    (
        r".*hashing.*nima.*",
        (
            "Hashing - bu ma'lumotlarni o'ziga xos qator yoki kodga aylantirish jarayoni bo'lib, u ko'pincha ma'lumotlarni indekslash va qidirishda ishlatiladi.",
            "Hashing yordamida ma'lumotlar tezroq qayta ishlanadi va ularni xavfsiz saqlash mumkin.",
            "Hashing kriptografiya va ma'lumotlar bazalarida keng qo'llaniladi.",
        ),
    ),

    # Ma'lumotlar bazasi nima?
    (
        r".*ma'lumotlar.*bazasi.*nima.*",
        (
            "Ma'lumotlar bazasi - bu ma'lumotlarni tuzilgan va samarali usulda saqlaydigan tizimdir.",
            "Ma'lumotlar bazasi yordamida katta hajmdagi ma'lumotlarni boshqarish va ularga kirish osonlashtiriladi.",
            "MySQL, PostgreSQL kabi tizimlar ma'lumotlar bazalarining namunalaridir.",
        ),
    ),

    # SQL va NoSQL farqi nima?
    (
        r".*sql.*va.*nosql.*farqi.*",
        (
            "SQL (Structured Query Language) strukturalangan ma'lumotlarni boshqarish uchun ishlatiladi, NoSQL esa turli formatlarda saqlanadigan ma'lumotlar uchun ishlatiladi.",
            "SQL relatsion ma'lumotlar bazalarida qo'llaniladi, NoSQL esa tez o'zgaruvchan va katta hajmdagi ma'lumotlar uchun.",
            "SQLda qat'iy tuzilgan ma'lumotlar bo'lsa, NoSQLda esa ko'proq moslashuvchanlik bor.",
        ),
    ),

    # Virtualizatsiya nima?
    (
        r".*virtualizatsiya.*nima.*",
        (
            "Virtualizatsiya - bu bitta fizik serverda bir nechta virtual serverlarni yaratish texnologiyasi.",
            "Virtualizatsiya orqali resurslardan samarali foydalanish va turli operatsion tizimlarni bir joyda ishga tushirish mumkin.",
            "Virtualizatsiya bulutli hisoblash va server boshqaruvini osonlashtiradi.",
        ),
    ),

    # Operating System (OS) nima?
    (
        r".*operatsion.*tizim.*nima.*",
        (
            "Operatsion tizim (OS) - bu kompyuter resurslarini boshqarish va dasturlarga kirish imkonini beradigan dasturiy ta'minotdir.",
            "Eng mashhur operatsion tizimlar: Windows, macOS, Linux, va Android.",
            "Operatsion tizim apparat va dasturiy ta'minot o'rtasida ko'prik vazifasini bajaradi.",
        ),
    ),

    # Docker nima?
    (
        r".*docker.*nima.*",
        (
            "Docker - bu dasturlarni izolyatsiyalangan konteynerlar ichida ishga tushirish imkonini beradigan platforma.",
            "Docker yordamida dasturlarni oson boshqarish, ko'chirish va joylashtirish mumkin.",
            "Docker konteynerlari dasturlar va ularning barcha bog'liqliklarini bir joyda saqlashga imkon beradi.",
        ),
    ),

    # Git nima?
    (
        r".*git.*nima.*",
        (
            "Git - bu versiya nazorati tizimi bo'lib, dasturlarni boshqarish va kod o'zgarishlarini kuzatish imkonini beradi.",
            "Git yordamida bir nechta dasturchilar bitta loyihada hamkorlikda ishlashlari mumkin.",
            "GitHub yoki GitLab kabi xizmatlar Git asosida loyihalarni boshqarish imkonini beradi.",
        ),
    ),

    # Kiberxavfsizlik nima?
    (
        r".*kiberxavfsizlik.*nima.*",
        (
            "Kiberxavfsizlik - bu kompyuter tizimlari va ma'lumotlarni xakerlik hujumlaridan himoya qilish jarayoni.",
            "Kiberxavfsizlik ma'lumotlarning maxfiyligini, yaxlitligini va mavjudligini ta'minlaydi.",
            "Shifrlash, xavfsizlik devorlari va antiviruslar kiberxavfsizlikning asosiy vositalaridir.",
        ),
    ),

        (
        r".*kompilyator.*nima.*",
        (
            "Kompilyator - bu dasturlash tilidagi kodni mashina tiliga aylantiradigan dasturdir.",
            "Kompilyator yordamida dastur kodini bajarish mumkin bo'lgan ko'rinishga keltiriladi.",
            "Kompilyatorlar C, C++, va boshqa ko'plab dasturlash tillarida ishlatiladi.",
        ),
    ),

    # Interpretor nima?
    (
        r".*interpretor.*nima.*",
        (
            "Interpretor - bu dastur kodini qadam-baqadam bajara oladigan dasturiy ta'minot.",
            "Interpretor kodni har bir qatorini tahlil qilib bajaradi, kompilyator esa kodni to'liq mashina tiliga aylantiradi.",
            "Python kabi yuqori darajadagi tillar interpretor yordamida ishlaydi.",
        ),
    ),

    # RAM nima?
    (
        r".*ram.*nima.*",
        (
            "RAM (Random Access Memory) - bu kompyuterning vaqtincha ma'lumotlarni saqlovchi qisqa muddatli xotirasi.",
            "RAM kompyuterning ishlash tezligini ta'minlaydi, ko'proq RAM bilan katta dasturlarni ishlatish osonroq.",
            "Operatsion tizim va dasturlar RAMda vaqtincha yuklanadi va ishga tushadi.",
        ),
    ),

    # ROM nima?
    (
        r".*rom.*nima.*",
        (
            "ROM (Read Only Memory) - bu kompyuterning doimiy xotirasi bo'lib, o'chirilmaydigan va o'zgartirib bo'lmaydigan ma'lumotlarni saqlaydi.",
            "ROM ichidagi ma'lumotlar kompyuter o'chirilganda ham saqlanib qoladi.",
            "BIOS kabi tizimlar ROMda saqlanadi.",
        ),
    ),

    # API nima?
    (
        r".*api.*nima.*",
        (
            "API (Application Programming Interface) - bu dasturlar va tizimlar o'rtasida aloqa qilish uchun ishlatiladigan interfeys.",
            "API yordamida dasturlar bir-birlari bilan ma'lumot almashishlari mumkin.",
            "API ko'pincha veb-xizmatlar va dasturlar o'rtasida aloqa o'rnatish uchun ishlatiladi.",
        ),
    ),

    # JSON nima?
    (
        r".*json.*nima.*",
        (
            "JSON (JavaScript Object Notation) - bu ma'lumotlarni almashish uchun foydalaniladigan oddiy va tushunarli format.",
            "JSON ko'pincha veb-ilovalar va serverlar o'rtasida ma'lumot uzatish uchun ishlatiladi.",
            "JSON fayllari yengil va inson o'qishi uchun qulay ko'rinishda bo'ladi.",
        ),
    ),

    # XML nima?
    (
        r".*xml.*nima.*",
        (
            "XML (eXtensible Markup Language) - bu ma'lumotlarni tuzilmalash va saqlash uchun foydalaniladigan format.",
            "XML fayllari tag-yozuvlar orqali ma'lumotlarni saqlaydi va tuzilgan ko'rinishga keltiradi.",
            "XML ko'pincha ma'lumotlarni uzatishda va saqlashda ishlatiladi.",
        ),
    ),

        (
        r".*(o'rganish|dasturlash).*",
        (
            "Dasturlashni o'rganish uchun oddiy til bilan boshlang, masalan, Python. Amaliyot qilishni unutmang.",
            "Onlayn kurslar va tutoriallar bilan boshlab, loyihalar yarating. Kodingizni tekshiring va yangilang.",
        ),
    ),

    # Yaxshi dasturchi
    (
        r".*(yaxshi|dasturchi).*",
        (
            "Yaxshi dasturchi bo'lish uchun doimiy o'rganish va yangi texnologiyalarni sinab ko'ring.",
            "Ochiq kodli loyihalarda ishtirok eting, bu sizga tajriba orttirishga yordam beradi.",
        ),
    ),

    # Dasturlash tili
    (
        r".*(qaysi|til|dasturlash).*",
        (
            "Python - boshlash uchun juda qulay, ko'p maqsadli dasturlash tili.",
            "Agar siz veb-dasturlashni o'rganmoqchi bo'lsangiz, JavaScript'dan boshlang.",
        ),
    ),

    # Algoritmlar
    (
        r".*(algoritm|murakkab).*",
        (
            "Algoritmlar ustida ishlash uchun muntazam mashq qiling va onlayn muammolarni yechishga harakat qiling.",
            "LeetCode, HackerRank kabi platformalarda turli muammolarni sinab ko'ring.",
        ),
    ),

    # Veb dasturchi bo'lish
    (
        r".*(veb|dasturchi).*",
        (
            "Veb dasturchi bo'lish uchun HTML, CSS va JavaScript tillarini o'rganing.",
            "Frontend va backend texnologiyalarning asoslarini o'zlashtirish muhim.",
        ),
    ),

    # Sun'iy intellekt o'rganish
    (
        r".*(sun'iy|intellekt).*",
        (
            "Sun'iy intellektni o'rganish uchun Python dasturlash tilida mashina o'rganish kutubxonalarini sinab ko'ring.",
            "Matematika va statistika asoslarini tushunish sun'iy intellektda juda muhim.",
        ),
    ),

    # Dastur yaratish
    (
        r".*(dastur|yaratish|loyiha).*",
        (
            "Dastur yaratish uchun loyiha rejasini tuzing va talablarni belgilang.",
            "Yaxshi kod tuzish va kodni tekshirishda qat'iy bo'ling.",
        ),
    ),

    # Yaxshi kod yozish
    (
        r".*(yaxshi|kod).*",
        (
            "Yaxshi kod yozish uchun toza va tushunarli nomlardan foydalaning, kodni qayerda bo'lsa ham izohlab bering.",
            "Kod optimallashtirish va samaradorlikni hisobga oling.",
        ),
    ),

    # Qaysi tillar kerak?
    (
        r".*(til|o'rganish|qaysi).*",
        (
            "Ma'lumotlar tahlili uchun Python, veb-dasturlash uchun JavaScript tilini o'rganishni tavsiya qilaman.",
            "Backend uchun Node.js yoki Django kabi tillardan foydalaning.",
        ),
    ),

    # Qanday qilib kodingizni yaxshilashingiz mumkin?
    (
        r".*(yaxshilash|kod).*",
        (
            "Kodingizni yaxshilash uchun uni qayta ko'rib chiqish va boshqa dasturchilardan fikr olish juda muhim.",
            "Modullardan foydalaning, murakkablikni kamaytirish va kodni qisqartirishga harakat qiling.",
        ),
    ),

    # Ma'lumotlar tuzilmalari
    (
        r".*(ma'lumotlar|tuzilmalar).*",
        (
            "Ma'lumotlar tuzilmalarini o'rganish uchun asosiy tushunchalarni o'zlashtiring: massivlar, ro'yxatlar, stacklar, va daraxtlar.",
            "Samarali algoritmlar yaratishda ma'lumotlar tuzilmalari juda muhimdir.",
        ),
    ),

    # Mobil dasturlash
    (
        r".*(mobil|dastur).*",
        (
            "Mobil dasturlash uchun Android uchun Kotlin yoki iOS uchun Swift o'rganishingiz mumkin.",
            "Mobil ilovalarni yaratishda foydalanuvchi tajribasiga katta e'tibor berish zarur.",
        ),
    ),

    # Git nima?
    (
        r".*(git|versiya).*",
        (
            "Git - bu versiya nazorati tizimi bo'lib, kodni boshqarish va tahlil qilish uchun ishlatiladi.",
            "GitHub kabi platformalarda ochiq manba loyihalarini ko'rib chiqish foydali bo'lishi mumkin.",
        ),
    ),

    # Docker va konteynerlash
    (
        r".*(docker|konteyner).*",
        (
            "Docker dasturlarni konteynerlar ichida ishga tushirish va boshqarish imkonini beradi.",
            "Konteynerlash orqali dasturiy ta'minotni izolyatsiyalash va uni samarali boshqarish mumkin.",
        ),
    ),

    # Bulutli hisoblash
    (
        r".*(bulut|hisoblash).*",
        (
            "Bulutli hisoblash orqali server va resurslarni oson boshqarish va ulardan samarali foydalanish mumkin.",
            "Google Cloud, AWS, yoki Azure kabi bulutli platformalarni o'rganishni tavsiya qilaman.",
        ),
    ),

    # O'rganish manbalari
    (
        r".*(manba|o'rganish).*",
        (
            "O'rganish uchun Codecademy, Coursera yoki Udemy kabi onlayn platformalarni sinab ko'ring.",
            "Bloglar, tutoriallar va ochiq manba kodlari o'rganishda yordam beradi.",
        ),
    ),

    # Loyihani qanday boshqarish kerak?
    (
        r".*(loyiha|boshqarish).*",
        (
            "Loyihani boshqarishda samarali rejalashtirish va versiya nazorati vositalaridan foydalaning.",
            "Kodning mustahkamligi va testlarga e'tibor qarating.",
        ),
    ),

    # Sun'iy intellekt yoki data science
    (
        r".*(intellekt|data|science).*",
        (
            "Sun'iy intellekt yoki data science o'rganish uchun numpy, pandas va sklearn kabi kutubxonalarni o'rganing.",
            "TensorFlow yoki PyTorch'dan foydalanib model yaratishni o'rganing.",
        ),
    ),

    # API nima?
    (
        r".*(api|interfeys).*",
        (
            "API (Application Programming Interface) dasturlar o'rtasida ma'lumot almashishga imkon beruvchi interfeysdir.",
            "RESTful API'lar bugungi kunda keng qo'llanilmoqda va JSON formatidan foydalaniladi.",
        ),
    ),

    # Mashina o'rganishi
    (
        r".*(mashina|o'rganish).*",
        (
            "Mashina o'rganish algoritmlarini o'rganish uchun Python dasturlash tilidan foydalaning.",
            "Sklearn bilan boshlang va keyinchalik chuqur o'rganish modellarini sinab ko'ring.",
        ),
    ),

    # Kriptografiya
    (
        r".*(kriptografiya|shifrlash).*",
        (
            "Kriptografiya ma'lumotlarni himoya qilish va ularni shifrlash orqali xavfsizlikni ta'minlaydi.",
            "AES va RSA shifrlash algoritmlari keng qo'llaniladi.",
        ),
    ),
)





chat = Chat(pairs)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = chat.respond(message)
        chat_history.append((message, bot_message))
        time.sleep(1)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch(share=True)