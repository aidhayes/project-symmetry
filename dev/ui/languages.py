import csv

# text = dict()


lang_eng = [
    "العربية",
    "বাংলা",
    "Български",
    "Bosanski",
    "Català",
    "Čeština",
    "Dansk",
    "Deutsch",
    "Eesti",
    "Ελληνικά",
    "English",
    "Español",
    "Esperanto",
    "Euskara",
    "فارسی",
    "Français",
    "Galego",
    "한국어",
    "Hrvatski",
    "Bahasa Indonesia",
    "Italiano",
    "עברית",
    "ქართული",
    "Latviešu",
    "Lietuvių",
    "Magyar",
    "Македонски",
    "Bahasa Melayu",
    "Nederlands",
    "日本語",
    "Norsk",
    "Polski",
    "Português",
    "Română",
    "Русский",
    "Slovenčina",
    "Slovenščina",
    "Српски / srpski",
    "Suomi",
    "Swedish",
    "ไทย",
    "Türkçe",
    "Українська",
    "Tiếng Việt",
    "中文"

]

# [Select language, Select, Wikipedia Article Comparison Tool, Compare, Select Comparison Tool, Select Similarity Percentage]
'''
with open("display.csv") as file:
     for line in csv.reader(file):
         text[line[0]] = line[2:]
'''

# print(text)
display_trans = {"العربية": ['اختار اللغة:', 'يختار', 'أداة مقارنة مقالة ويكيبيديا', 'قارن', 'حدد أداة المقارنة:', 'حدد النسبة المئوية للتشابه:', 'يترجم', 'صافي'], 'বাংলা': ['ভাষা নির্বাচন কর:', 'নির্বাচন করুন', 'উইকিপিডিয়া নিবন্ধ তুলনা সরঞ্জাম', 'তুলনা করা', 'তুলনা সরঞ্জাম নির্বাচন করুন:', 'সাদৃশ্য শতাংশ নির্বাচন করুন:', 'অনুবাদ করা', 'স্পষ্ট'], 'Euskara': ['Hautatu Hizkuntza:', 'Hautatu', 'Wikipedia artikuluaren konparazio tresna', 'Alderatu', 'Hautatu Konparaziorako tresna:', 'Aukeratu antzekotasun portzentajea:', 'Itzuli', 'Hustu'], 'Bosanski': ['Odaberite Jezik:', 'Odabrati', 'Alat za upoređivanje članaka Wikipedia', 'Uporediti', 'Odaberite sredstvo za usporedbu:', 'Odaberite postotak sličnosti:', 'Prevesti', 'Jasan'], 'Български': ['Избери език:', 'Изберете', 'Инструмент за сравнение на статии в Уикипедия', 'Сравнете', 'Изберете инструмент за сравнение:', 'Изберете Процент на сходство:', 'Превод', 'Ясно'], 'Català': ["Escolliu l'idioma:", 'Seleccionar', "Eina de comparació de l'article de Viquipèdia", 'Comparar', "Seleccioneu l'eina de comparació:", 'Seleccioneu percentatge de similitud:', 'Traduir', 'Clar'], '中文': ['选择语言：', '选择', 'Wikipedia文章比较工具', '相比', '选择比较工具：', '选择相似性百分比：', '翻译', '清除'], 'Hrvatski': ['Izaberi jezik:', 'Odaberi', 'Wikipedia Alat za usporedbu članka', 'Usporediti', 'Odaberite Alat za usporedbu:', 'Odaberite postotak sličnosti:', 'Prevedi', 'Čisto'], 'Čeština': ['Zvolte jazyk:', 'Vybrat', 'Nástroj pro srovnání článků Wikipedia', 'Porovnat', 'Vyberte Porovnání nástroje:', 'Vyberte procento podobnosti:', 'přeložit', 'Průhledná'], 'Dansk': ['Vælg sprog:', 'Vælg', 'Wikipedia Artikel sammenligningsværktøj', 'Sammenligne', 'Vælg sammenligningsværktøj:', 'Vælg lighedsprocent:', 'Oversætte', 'Klar'], 'Nederlands': ['Selecteer taal:', 'Uitkiezen', 'Wikipedia artikelvergelijkingstool', 'Vergelijken', 'Selecteer Vergelijkingstool:', 'Selecteer gelijkenispercentage:', 'Vertalen', 'Duidelijk'], 'English': ['Select Language:', 'Select', 'Wikipedia Article Comparison Tool', 'Compare', 'Select comparison tool:', 'Select similarity percentage:', 'Translate', 'Clear'], 'Esperanto': ['Elektu Lingvon:', 'Elektu', 'Vikipedio Artikola Kompara Ilo', 'Komparu', 'Elektu Kompara Ilo:', 'Elektu Similecan Procenton:', 'Traduki', 'Klara'], 'Eesti': ['Vali keel:', 'Valima', 'Vikipeedia artikli võrdlusvahend', 'Võrdlema', 'Valige võrdlusriist:', 'Valige sarnasuse protsent:', 'Tõlkima', 'Selge'], 'Suomi': ['Valitse kieli:', 'Valita', 'Wikipedia -artikkelin vertailutyökalu', 'Vertailla', 'Valitse vertailutyökalu:', 'Valitse samankaltaisuusprosentti:', 'Kääntää', 'Asia selvä'], 'Français': ['Choisir la langue:', 'Sélectionner', "Outil de comparaison de l'article Wikipedia", 'Comparer', "Sélectionnez l'outil de comparaison:", 'Sélectionnez le pourcentage de similitude:', 'Traduire', 'Dégager'], 'Galego': ['Selecciona Idioma:', 'Selecciona', 'Ferramenta de comparación de artigos de Wikipedia', 'Comparar', 'Seleccione Ferramenta de comparación:', 'Selecciona porcentaxe de semellanza:', 'Traducir', 'Claro'], 'ქართული': ['Აირჩიეთ ენა:', 'გადარჩევა', 'ვიკიპედიის სტატიის შედარების ინსტრუმენტი', 'შედარება', 'აირჩიეთ შედარების ინსტრუმენტი:', 'აირჩიეთ მსგავსების პროცენტი:', 'თარგმნა', 'გასუფთავება'], 'Deutsch': ['Sprache auswählen:', 'Auswählen', 'Wikipedia -Artikelvergleichsinstrument', 'Vergleichen', 'Wählen Sie Vergleichswerkzeug:', 'Wählen Sie Ähnlichkeitsprozentsatz:', 'Übersetzen', 'Klar'], 'Ελληνικά': ['Επιλέξτε γλώσσα:', 'Επιλέγω', 'Εργαλείο σύγκρισης άρθρων Wikipedia', 'Συγκρίνω', 'Επιλέξτε εργαλείο σύγκρισης:', 'Επιλέξτε Ποσοστό ομοιότητας:', 'Μεταφράζω', 'Σαφή'], 'עברית': ['בחר שפה:', 'בחר', 'כלי השוואת מאמרים בוויקיפדיה', 'לְהַשְׁווֹת', 'בחר בכלי השוואה:', 'בחר אחוז דמיון:', 'תרגם', 'ברור'], 'Magyar': ['Válasszon nyelvet:', 'Válasszon', 'Wikipedia cikk összehasonlító eszköz', 'Összehasonlít', 'Válassza ki az összehasonlító eszközt:', 'Válassza ki a hasonlósági százalékot:', 'fordít', 'Egyértelmű'], 'Bahasa Indonesia': ['Pilih bahasa:', 'Pilih', 'Alat Perbandingan Artikel Wikipedia', 'Membandingkan', 'Pilih Alat Perbandingan:', 'Pilih persentase kesamaan:', 'Menerjemahkan', 'Jernih'], 'Italiano': ['Seleziona la lingua:', 'Selezionare', 'Strumento di confronto degli articoli di Wikipedia', 'Confrontare', 'Seleziona lo strumento di confronto:', 'Seleziona percentuale di somiglianza:', 'Tradurre', 'Chiaro'], '日本語': ['言語を選択する：', '選択する', 'ウィキペディアの記事比較ツール', '比較', '比較ツールを選択します：', '類似性の割合を選択します：', '翻訳', 'クリア'], '한국어': ['언어 선택 :', '고르다', 'Wikipedia 기사 비교 도구', '비교하다', '비교 도구 선택 :', '유사성 백분율 선택 :', '번역하다', '분명한'], 'Latviešu': ['Izvēlēties valodu:', 'Atlasīt', 'Wikipedia rakstu salīdzināšanas rīks', 'Salīdzināt', 'Atlasīt salīdzināšanas rīku:', 'Izvēlieties līdzības procentuālo daudzumu:', 'Tulkot', 'Noskaidrot'], 'Lietuvių': ['Pasirinkite kalbą:', 'Pasirinkite', 'Vikipedijos straipsnių palyginimo įrankis', 'Palyginkite', 'Pasirinkite palyginimo įrankį:', 'Pasirinkite panašumo procentą:', 'Išversti', 'Aišku'], 'Македонски': ['Одбери јазик:', 'Изберете', 'Алатка за споредување на статии на Википедија', 'Споредете', 'Изберете алатка за споредување:', 'Изберете процент на сличност:', 'Преведете', 'Чиста'], 'Bahasa Melayu': ['Pilih Bahasa:', 'Pilih', 'Alat Perbandingan Artikel Wikipedia', 'Bandingkan', 'Pilih Alat Perbandingan:', 'Pilih Peratusan Persamaan:', 'Terjemahkan', 'Jelas'], 'Norsk': ['Velg språk:', 'Å velge', 'Wikipedia -artikkel Sammenligningsverktøy', 'Sammenligne', 'Velg sammenligningsverktøy:', 'Velg likhetsprosent:', 'Oversette', 'Klar'], 'فارسی': ['زبان را انتخاب کنید:', 'انتخاب کنید', 'ابزار مقایسه مقاله ویکی پدیا', 'مقایسه کردن', 'ابزار مقایسه را انتخاب کنید:', 'درصد شباهت را انتخاب کنید:', 'ترجمه کردن', 'پاک کردن'], 'Polski': ['Wybierz język:', 'Wybierz', 'Narzędzie do porównywania artykułów w Wikipedii', 'Porównywać', 'Wybierz narzędzie porównawcze:', 'Wybierz Procent podobieństwa:', 'Tłumaczyć', 'Jasne'], 'Português': ['Selecione o idioma:', 'Selecione', 'Ferramenta de comparação de artigos da Wikipedia', 'Comparar', 'Selecione Ferramenta de comparação:', 'Selecione porcentagem de similaridade:', 'Traduzir', 'Claro'], 'Română': ['Selecteaza limba:', 'Selectați', 'Instrument de comparare a articolului Wikipedia', 'Comparaţie', 'Selectați instrument de comparație:', 'Selectați procentul de similaritate:', 'Traduceți', 'clar'], 'Русский': ['Выберите язык:', 'Выбирать', 'Инструмент сравнения статей в Википедии', 'Сравнивать', 'Выберите инструмент сравнения:', 'Выберите процент сходства:', 'Перевести', 'чистый'], 'Српски': ['Изаберите језик:', 'Одабрати', 'Алат за поређење чланака Википедије', 'Упоредити', 'Изаберите Алат за поређење:', 'Изаберите проценат сличности:', 'превести', 'Јасно'], 'Slovenčina': ['Zvoľ jazyk:', 'Vybraný', 'Porovnanie článku Wikipedia', 'Porovnať', 'Vyberte porovnávací nástroj:', 'Vyberte percento podobnosti:', 'Preložiť', 'jasný'], 'Slovenščina': ['Izberi jezik:', 'Izberite', 'Orodje za primerjavo članka Wikipedije', 'Primerjaj', 'Izberite Primerjalno orodje:', 'Izberite Odstotek podobnosti:', 'Prevesti', 'Jasno'], 'Español': ['Seleccione el idioma:', 'Seleccione', 'Herramienta de comparación de artículos de Wikipedia', 'Comparar', 'Seleccione la herramienta de comparación:', 'Seleccionar porcentaje de similitud:', 'Traducir', 'Claro'], 'Svenska': ['Välj språk:', 'Välj', 'Wikipedia artikeljämförelseverktyg', 'Jämföra', 'Välj jämförelseverktyg:', 'Välj likhetsprocent:', 'Översätt', 'Klar'], 'ไทย': ['เลือกภาษา:', 'เลือก', 'เครื่องมือเปรียบเทียบบทความ Wikipedia', 'เปรียบเทียบ', 'เลือกเครื่องมือเปรียบเทียบ:', 'เลือกเปอร์เซ็นต์ความคล้ายคลึงกัน:', 'แปลภาษา', 'ชัดเจน'], 'Türkçe': ['Dil Seçin:', 'Seçme', 'Wikipedia makale karşılaştırma aracı', 'Karşılaştırmak', 'Karşılaştırma aracını seçin:', 'Benzerlik yüzdesini seçin:', 'Çevirmek', 'Temizlemek'], 'Українська': ['Оберіть мову:', 'Обраний', 'Інструмент порівняння статті Вікіпедії', 'Порівнювати', 'Виберіть інструмент порівняння:', 'Виберіть відсоток подібності:', 'Перекладати', 'Чіткий'], 'Tiếng Việt': ['Chọn ngôn ngữ:', 'Lựa chọn', 'Công cụ so sánh bài viết Wikipedia', 'So sánh', 'Chọn Công cụ so sánh:', 'Chọn Tỷ lệ phần trăm tương tự:', 'Dịch', 'Xa lạ']}
